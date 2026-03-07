document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send-btn');
    const resetBtn = document.getElementById('reset-btn');
    const packet = document.getElementById('packet');
    const packetContent = packet.querySelector('.packet-content');

    const simTitle = document.getElementById('sim-step-title');
    const simDesc = document.getElementById('sim-step-desc');

    const layers = [
        { id: 'layer-application', title: 'Application Layer', desc: 'Creates HTTP request data.', content: 'HTTP Data', bg: 'var(--layer-7)' },
        { id: 'layer-presentation', title: 'Presentation Layer', desc: 'Encrypts and compresses the data (e.g., TLS).', content: 'Encrypted Data', bg: 'var(--layer-6)' },
        { id: 'layer-session', title: 'Session Layer', desc: 'Establishes and manages the session.', content: 'Session Data', bg: 'var(--layer-5)' },
        { id: 'layer-transport', title: 'Transport Layer', desc: 'Adds TCP header with source and destination ports.', content: 'TCP Segment', bg: 'var(--layer-4)' },
        { id: 'layer-network', title: 'Network Layer', desc: 'Adds IP header with logical routing addresses.', content: 'IP Packet', bg: 'var(--layer-3)' },
        { id: 'layer-data-link', title: 'Data Link Layer', desc: 'Adds MAC addresses to form a frame.', content: 'Ethernet Frame', bg: 'var(--layer-2)' },
        { id: 'layer-physical', title: 'Physical Layer', desc: 'Converts the frame into bits for transmission.', content: '01010101', bg: 'var(--layer-1)' }
    ];

    let currentStep = 0;
    let animationInterval = null;

    function resetSimulation() {
        if (animationInterval) clearInterval(animationInterval);
        packet.style.opacity = '0';
        packet.style.top = '76px';
        packet.style.backgroundColor = 'var(--secondary-color)';
        packetContent.textContent = 'Data';

        document.querySelectorAll('.sim-layer').forEach(l => l.classList.remove('active'));

        simTitle.textContent = 'Ready';
        simDesc.textContent = 'Click "Send Packet" to begin the simulation.';

        currentStep = 0;
        sendBtn.disabled = false;
        resetBtn.disabled = true;
    }

    sendBtn.addEventListener('click', () => {
        sendBtn.disabled = true;
        resetBtn.disabled = false;

        packet.style.opacity = '1';

        animationInterval = setInterval(() => {
            if (currentStep >= layers.length) {
                clearInterval(animationInterval);
                simTitle.textContent = 'Transmission Complete';
                simDesc.textContent = 'The bits are now traveling over the physical medium.';
                packet.style.opacity = '0'; // Disappear
                return;
            }

            const layerInfo = layers[currentStep];

            // Highlight layer
            document.querySelectorAll('.sim-layer').forEach(l => l.classList.remove('active'));
            document.getElementById(layerInfo.id).classList.add('active');

            // Move packet
            const offset = 76 + (currentStep * 41); // Roughly aligns with the CSS gap and height
            packet.style.top = `${offset}px`;

            // Update Packet content
            packetContent.textContent = layerInfo.content;
            packet.style.backgroundColor = layerInfo.bg;

            // Update explanation
            simTitle.textContent = layerInfo.title;
            simDesc.textContent = layerInfo.desc;

            currentStep++;
        }, 1500); // 1.5 seconds per step
    });

    resetBtn.addEventListener('click', resetSimulation);
});
