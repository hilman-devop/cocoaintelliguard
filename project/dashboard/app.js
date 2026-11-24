// CocoaIntelliGuard - Dashboard Logic & Firebase Client

// 1. Firebase Configuration (Ganti dengan konfigurasi Firebase Anda)
const firebaseConfig = {
    databaseURL: "https://your-project-default-rtdb.firebaseio.com" // Ubah sesuai Realtime Database Anda
};

// State Global
let isDemoMode = true;
let totalScans = 1644;
let healthyCount = 668;
let diseasedCount = 976;
let databaseRef = null;
let diseaseChartInstance = null;
let leafletMap = null;
let mapMarkers = [];

// Koordinat Pusat Kebun (lokasi uji lapangan / lokasi uji lapangan)
const DEMO_COORDS = [0, 0];

// Data Rekomendasi Penanganan Penyakit Kakao
const RECOMMENDATIONS = {
    busuk_buah: {
        title: "Busuk Buah Kakao (Black Pod Disease)",
        desc: "Disebabkan oleh jamur Phytophthora palmivora. Jamur ini berkembang sangat cepat pada kondisi kelembaban tinggi dan curah hujan rata-rata di atas 2000 mm/tahun.",
        steps: [
            "Lakukan sanitasi kebun secara berkala dengan memangkas buah yang membusuk agar tidak menular ke buah sehat lainnya.",
            "Lakukan pemangkasan bentuk pelindung agar sinar matahari bisa masuk secara optimal (menurunkan kelembaban mikro kebun).",
            "Gunakan penyemprotan fungisida berbasis tembaga (0.3%) pada permukaan buah secara merata jika tingkat serangan di kebun >15%."
        ]
    },
    vsd: {
        title: "Vascular Streak Dieback (VSD)",
        desc: "Disebabkan oleh jamur Ceratobasidium theobromae yang menyerang pembuluh kayu (xilem) daun muda dan ranting kakao, menghambat jalannya zat hara.",
        steps: [
            "Potong cabang/ranting yang terinfeksi minimal 30 cm di bawah titik bagian kayu yang berubah warna kecokelatan.",
            "Lakukan pemupukan seimbang (NPK + pupuk organik) secara rutin untuk memperkuat daya tahan internal tanaman kakao.",
            "Gunakan klon kakao tahan VSD (seperti klon Sulawesi 1, Sulawesi 2, ICCRI 07) untuk rehabilitasi tanaman."
        ]
    },
    kanker_batang: {
        title: "Kanker Batang Kakao",
        desc: "Disebabkan oleh patogen Phytophthora palmivora yang menyerang kulit batang utama atau cabang. Menimbulkan luka busuk basah kehitaman yang mengeluarkan cairan cokelat kemerahan.",
        steps: [
            "Kerok bagian kulit batang yang membusuk sampai batas kulit yang sehat (berwarna hijau kekuningan).",
            "Oleskan fungisida kontak berbahan aktif tembaga klorida atau bubur Bordeaux pada luka kerokan.",
            "Pastikan sistem drainase kebun berjalan baik agar tidak ada air menggenang di sekitar pangkal batang pohon kakao."
        ]
    }
};

// 2. Inisialisasi Firebase
try {
    if (firebaseConfig.databaseURL && !firebaseConfig.databaseURL.includes("default-rtdb")) {
        firebase.initializeApp(firebaseConfig);
        const database = firebase.database();
        databaseRef = database.ref("detections");
        isDemoMode = false;
        document.getElementById("connection-status").innerText = "Terkoneksi ke Firebase Database";
        document.getElementById("connection-status").parentElement.classList.add("connected");
        console.log("[INFO] Firebase berhasil diinisialisasi.");
    } else {
        console.log("[INFO] Menggunakan Demo Mode (Simulasi Data Real-time).");
        setupDemoMode();
    }
} catch (e) {
    console.warn("[WARNING] Gagal memuat Firebase SDK. Berpindah ke Demo Mode.", e);
    setupDemoMode();
}

// 3. Inisialisasi Grafik Chart.js
function initChart() {
    const ctx = document.getElementById('diseaseChart').getContext('2d');
    
    // Gradient untuk area chart
    const healthyGradient = ctx.createLinearGradient(0, 0, 0, 300);
    healthyGradient.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
    healthyGradient.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
    
    const diseasedGradient = ctx.createLinearGradient(0, 0, 0, 300);
    diseasedGradient.addColorStop(0, 'rgba(244, 63, 94, 0.4)');
    diseasedGradient.addColorStop(1, 'rgba(244, 63, 94, 0.0)');

    diseaseChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'],
            datasets: [
                {
                    label: 'Kakao Sehat',
                    data: [85, 92, 78, 110, 95, 105, 103],
                    borderColor: '#10b981',
                    borderWidth: 3,
                    backgroundColor: healthyGradient,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#10b981'
                },
                {
                    label: 'Terinfeksi Penyakit',
                    borderColor: '#f43f5e',
                    borderWidth: 3,
                    data: [42, 38, 55, 30, 48, 62, 50],
                    backgroundColor: diseasedGradient,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: '#f43f5e'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: '#94a3b8',
                        font: { family: 'Fira Sans', size: 12 }
                    }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(255, 255, 255, 0.03)' },
                    ticks: { color: '#64748b', font: { family: 'Fira Sans' } }
                },
                y: {
                    grid: { color: 'rgba(255, 255, 255, 0.03)' },
                    ticks: { color: '#64748b', font: { family: 'Fira Sans' } }
                }
            }
        }
    });
}

// 4. Inisialisasi Peta Leaflet.js
function initMap() {
    // Buat Peta terpusat di lokasi uji lapangan
    leafletMap = L.map('map').setView(DEMO_COORDS, 16);

    // Tile Layer peta gelap premium (CartoDB Dark Matter)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(leafletMap);

    // Titik default instrumen alat CocoaIntelliGuard (Pusat Kebun)
    L.marker(DEMO_COORDS).addTo(leafletMap)
        .bindPopup("<b>CocoaIntelliGuard Node 1</b><br>Lokasi Base Station Utama.")
        .openPopup();
}

// 5. Logika Simulasi Demo Mode (Real-time Simulation)
function setupDemoMode() {
    isDemoMode = true;
    document.getElementById("connection-status").innerText = "Mode Simulasi (Offline/Demo)";
    document.getElementById("connection-status").parentElement.classList.remove("connected");
    
    // Inisialisasi log riwayat default
    const mockDetections = [
        { time: "01:15:32", diagnosis: "Kakao Sehat", confidence: 99.3, lat: 0.0002, lng: 0.0002 },
        { time: "01:12:45", diagnosis: "Busuk Buah", confidence: 96.5, lat: -0.0002, lng: -0.0002 },
        { time: "01:08:12", diagnosis: "VSD", confidence: 92.4, lat: 0.0003, lng: -0.0003 },
        { time: "01:02:50", diagnosis: "Kanker Batang", confidence: 95.1, lat: -0.0003, lng: 0.0003 }
    ];

    mockDetections.forEach(data => {
        addLogToTable(data.time, data.diagnosis, data.confidence, `${data.lat.toFixed(4)}, ${data.lng.toFixed(4)}`);
        addMapMarker(data.lat, data.lng, data.diagnosis, data.confidence);
    });

    // Simulasi penambahan data setiap 8 detik
    setInterval(() => {
        const diseases = ["Kakao Sehat", "Busuk Buah", "VSD", "Kanker Batang"];
        const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];
        const confidence = (85 + Math.random() * 14.8).toFixed(1);
        
        // Random koordinat di sekitar kebun
        const lat = DEMO_COORDS[0] + (Math.random() - 0.5) * 0.003;
        const lng = DEMO_COORDS[1] + (Math.random() - 0.5) * 0.003;
        
        const now = new Date();
        const timeStr = now.toTimeString().split(" ")[0];

        // Update stats
        totalScans++;
        if (randomDisease === "Kakao Sehat") {
            healthyCount++;
        } else {
            diseasedCount++;
        }
        updateStatsUI();

        // Tambahkan data ke tabel & peta
        addLogToTable(timeStr, randomDisease, confidence, `${lat.toFixed(4)}, ${lng.toFixed(4)}`);
        addMapMarker(lat, lng, randomDisease, confidence);

        // Update chart (tambahkan ke hari minggu)
        if (diseaseChartInstance) {
            const chartData = diseaseChartInstance.data.datasets;
            if (randomDisease === "Kakao Sehat") {
                chartData[0].data[6]++;
            } else {
                chartData[1].data[6]++;
            }
            diseaseChartInstance.update();
        }
    }, 8000);
}

// 6. Listener Data Real-time Firebase
if (databaseRef) {
    databaseRef.limitToLast(20).on("child_added", (snapshot) => {
        const val = snapshot.val();
        if (val) {
            const timestamp = val.timestamp ? new Date(val.timestamp).toLocaleTimeString() : new Date().toLocaleTimeString();
            const confidence = val.confidence ? (val.confidence * 100).toFixed(1) : "95.0";
            const location = val.latitude && val.longitude ? `${val.latitude.toFixed(4)}, ${val.longitude.toFixed(4)}` : "Internal GPS";
            
            // Increment counters
            totalScans++;
            if (val.diagnosis === "Kakao Sehat") {
                healthyCount++;
            } else {
                diseasedCount++;
            }
            updateStatsUI();

            // Tambah tabel & peta
            addLogToTable(timestamp, val.diagnosis, confidence, location);
            if (val.latitude && val.longitude) {
                addMapMarker(val.latitude, val.longitude, val.diagnosis, confidence);
            }
        }
    });
}

// 7. Helper UI Functions
function updateStatsUI() {
    document.getElementById("stat-total-scans").innerText = totalScans.toLocaleString();
    document.getElementById("stat-healthy").innerText = healthyCount.toLocaleString();
    document.getElementById("stat-diseased").innerText = diseasedCount.toLocaleString();
    
    const pct = ((diseasedCount / totalScans) * 100).toFixed(1);
    document.getElementById("stat-diseased-pct").innerText = `${pct}% Butuh Penanganan`;
}

function addLogToTable(time, diagnosis, confidence, location) {
    const tableBody = document.getElementById("log-table-body");
    const isHealthy = diagnosis === "Kakao Sehat";
    const badgeClass = isHealthy ? "badge-sehat" : "badge-penyakit";
    
    const newRow = document.createElement("tr");
    newRow.innerHTML = `
        <td>${time}</td>
        <td><span class="badge ${badgeClass}">${diagnosis}</span></td>
        <td>${confidence}%</td>
        <td><code>${location}</code></td>
        <td style="color: ${isHealthy ? '#10b981' : '#f43f5e'}">${isHealthy ? 'Aman' : 'Tindakan'}</td>
    `;
    
    // Sisipkan di atas sendiri agar data terbaru ada di paling atas
    tableBody.insertBefore(newRow, tableBody.firstChild);

    // Batasi baris tabel maksimal 15 agar tidak penuh
    if (tableBody.children.length > 15) {
        tableBody.removeChild(tableBody.lastChild);
    }
}

function addMapMarker(lat, lng, diagnosis, confidence) {
    if (!leafletMap) return;

    const isHealthy = diagnosis === "Kakao Sehat";
    const markerColor = isHealthy ? "#10b981" : "#f43f5e";
    
    // Buat lingkaran marker custom
    const marker = L.circleMarker([lat, lng], {
        radius: 8,
        fillColor: markerColor,
        color: "#ffffff",
        weight: 1.5,
        opacity: 1,
        fillOpacity: 0.8
    }).addTo(leafletMap);

    marker.bindPopup(`
        <div style="font-family: 'Outfit', sans-serif;">
            <b style="color: ${markerColor}; font-size: 14px;">${diagnosis}</b><br>
            Akurasi: <b>${confidence}%</b><br>
            Koordinat: <code>${lat.toFixed(5)}, ${lng.toFixed(5)}</code>
        </div>
    `);

    mapMarkers.push(marker);

    // Pan peta ke lokasi marker baru secara halus
    leafletMap.panTo([lat, lng]);
}

// 8. Logika Switcher Rekomendasi Penanganan
function switchRec(key, element) {
    const data = RECOMMENDATIONS[key];
    if (!data) return;

    // Toggle active state button
    const buttons = document.querySelectorAll(".rec-tab-btn");
    buttons.forEach(btn => btn.classList.remove("active"));
    
    if (element) {
        element.classList.add("active");
    } else {
        const indexMap = { busuk_buah: 0, vsd: 1, kanker_batang: 2 };
        const idx = indexMap[key];
        if (buttons[idx]) {
            buttons[idx].classList.add("active");
        }
    }

    // Render konten rekomendasi
    const container = document.getElementById("rec-display-content");
    
    let listHTML = "";
    data.steps.forEach(step => {
        listHTML += `<li>${step}</li>`;
    });

    container.innerHTML = `
        <div class="rec-title">${data.title}</div>
        <div class="rec-desc">${data.desc}</div>
        <div class="rec-steps-title">Langkah Tindak Lanjut:</div>
        <ul class="rec-steps">
            ${listHTML}
        </ul>
    `;
}

// Inisialisasi awal saat halaman di-load
window.addEventListener("DOMContentLoaded", () => {
    initChart();
    initMap();
    // Default load rekomendasi busuk buah
    switchRec("busuk_buah");
});
