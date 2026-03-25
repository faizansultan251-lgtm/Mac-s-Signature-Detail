document.addEventListener('DOMContentLoaded', () => {
    
    // --- Canvas Particles (Sparks) ---
    const canvas = document.getElementById('sparks-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = document.getElementById('hero').offsetHeight;

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = document.getElementById('hero').offsetHeight;
        });

        const particles = [];
        const numParticles = 80;

        class Particle {
            constructor() {
                this.x = Math.random() * width;
                this.y = height + Math.random() * 200;
                this.vx = (Math.random() - 0.5) * 1;
                this.vy = -Math.random() * 2 - 0.5;
                this.size = Math.random() * 2.5 + 0.5;
                this.opacity = Math.random() * 0.8 + 0.2;
                this.color = Math.random() > 0.5 ? `rgba(0, 163, 255, ${this.opacity})` : `rgba(226, 232, 240, ${this.opacity})`;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;
                if (Math.random() > 0.95) this.vx += (Math.random() - 0.5) * 0.5;
                if (this.y < -10) {
                    this.y = height + 10;
                    this.x = Math.random() * width;
                }
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.fill();
            }
        }

        for (let i = 0; i < numParticles; i++) {
            particles.push(new Particle());
        }

        function animateSparks() {
            ctx.clearRect(0, 0, width, height);
            particles.forEach(p => {
                p.update();
                p.draw();
            });
            requestAnimationFrame(animateSparks);
        }
        animateSparks();
    }

    // --- Scroll Animations (Intersection Observer) ---
    const revalElements = document.querySelectorAll('.reveal-up');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    revalElements.forEach(el => {
        revealObserver.observe(el);
    });


    // --- Floating Chatbot Logic ---
    const chatToggleBtn = document.getElementById('chatbot-toggle');
    const chatWindow = document.getElementById('chatbot-window');
    const chatCloseBtn = document.getElementById('chatbot-close');
    const optionsContainer = document.getElementById('chatbot-options');
    const messagesContainer = document.getElementById('chatbot-messages');
    
    let isChatOpen = false;

    const qaDatabase = [
        {
            q: "What services do you offer?",
            a: "We offer Exterior Detail, Interior Detail, Ceramic Coatings & Polishing, Polishing, Maintenance Details (In/Ex), and Add-On Services like headlight restore, steam cleaning, and odor/stain removal."
        },
        {
            q: "How much is an exterior detail?",
            a: "Exterior Detail starts at $80 for Coupe/Sedans, $100 for SUV's/Pickup Trucks, and $120 for Large Trucks/Vans."
        },
        {
            q: "How much is an interior detail?",
            a: "Interior Detail starts at $40 for Coupe/Sedans, $60 for SUV's/Pickup Trucks, and $80 for Large Trucks/Vans."
        },
        {
            q: "What about ceramic coatings?",
            a: "Ceramic Coatings & Polishing starts at $750 for Cars, $850 for SUVs, and $950 for Large Trucks/Vans."
        },
        {
            q: "Do you offer maintenance plans?",
            a: "Yes! Maintenance Details (In/Ex) start at $80 for Coupe/Sedans, $100 for SUV/Pickup Trucks, and $120 for Large Trucks/Vans. We offer weekly, biweekly, and monthly options."
        },
        {
            q: "How do I book?",
            a: "You can book by using the website's booking form, calling us directly at +1 561-788-2872, or emailing macdetailing25@gmail.com."
        },
        {
            q: "How do I contact you?",
            a: "You can reach Mac's Signature Auto Care at +1 561-788-2872 or email macdetailing25@gmail.com."
        }
    ];

    function toggleChat() {
        isChatOpen = !isChatOpen;
        if (isChatOpen) {
            chatWindow.classList.remove('hidden');
            chatToggleBtn.style.transform = 'scale(0) opacity(0)';
            setTimeout(() => chatToggleBtn.style.display = 'none', 300);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        } else {
            chatWindow.classList.add('hidden');
            chatToggleBtn.style.display = 'flex';
            setTimeout(() => chatToggleBtn.style.transform = 'scale(1)', 10);
        }
    }

    chatToggleBtn.addEventListener('click', toggleChat);
    chatCloseBtn.addEventListener('click', toggleChat);

    function initChatOptions() {
        optionsContainer.innerHTML = '';
        qaDatabase.forEach((item, index) => {
            const chip = document.createElement('button');
            chip.className = 'chat-chip';
            chip.innerText = item.q;
            chip.addEventListener('click', () => handleChatOptionClick(item));
            optionsContainer.appendChild(chip);
        });
    }

    function addMessage(text, isBot = true) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${isBot ? 'bot-message' : 'user-message'}`;
        msgDiv.innerText = text;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function handleChatOptionClick(item) {
        addMessage(item.q, false);
        const chips = document.querySelectorAll('.chat-chip');
        chips.forEach(chip => chip.style.pointerEvents = 'none');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.innerText = '...';
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        setTimeout(() => {
            typingDiv.remove();
            addMessage(item.a, true);
            chips.forEach(chip => chip.style.pointerEvents = 'auto');
        }, 800);
    }

    initChatOptions();

    // --- Before/After Slider Logic ---
    const sliderContainer = document.getElementById('slider-container');
    const beforeImg = document.getElementById('before-img');
    const sliderHandle = document.getElementById('slider-handle');

    if (sliderContainer && beforeImg && sliderHandle) {
        let isDragging = false;
        
        const updateSlider = (e) => {
            if (!isDragging) return;
            const rect = sliderContainer.getBoundingClientRect();
            let x = 0;
            if (e.type && e.type.includes('touch')) {
                x = e.touches[0].clientX - rect.left;
            } else {
                x = e.clientX - rect.left;
            }
            let position = (x / rect.width) * 100;
            position = Math.max(0, Math.min(position, 100));
            
            beforeImg.style.clipPath = `polygon(0 0, ${position}% 0, ${position}% 100%, 0 100%)`;
            sliderHandle.style.left = `${position}%`;
        };

        sliderContainer.addEventListener('mousedown', () => isDragging = true);
        window.addEventListener('mouseup', () => isDragging = false);
        window.addEventListener('mousemove', updateSlider);

        sliderContainer.addEventListener('touchstart', (e) => {
            isDragging = true;
            updateSlider(e);
        }, {passive: true});
        window.addEventListener('touchend', () => isDragging = false);
        window.addEventListener('touchmove', updateSlider, {passive: true});
        
        setTimeout(() => {
            beforeImg.style.transition = 'clip-path 1.5s cubic-bezier(0.165, 0.84, 0.44, 1)';
            sliderHandle.style.transition = 'left 1.5s cubic-bezier(0.165, 0.84, 0.44, 1)';
            beforeImg.style.clipPath = 'polygon(0 0, 75% 0, 75% 100%, 0 100%)';
            sliderHandle.style.left = '75%';
            
            setTimeout(() => {
                beforeImg.style.transition = 'none';
                sliderHandle.style.transition = 'none';
            }, 1500);
        }, 800);
    }

});


// ===== INSTANT QUOTE CALCULATOR =====

// Pricing matrix: service -> vehicle -> price
const pricingMatrix = {
    exterior: {
        sedan: 80,
        suv: 100,
        large: 120,
        utv: 80  // UTV $120 / ATV $80, using base $80
    },
    interior: {
        sedan: 40,
        suv: 60,
        large: 80,
        utv: null // Not applicable
    },
    ceramic: {
        sedan: 750,
        suv: 850,
        large: 950,
        utv: null
    },
    polishing: {
        sedan: 350,
        suv: 450,
        large: 550,
        utv: null
    },
    maintenance: {
        sedan: 80,
        suv: 100,
        large: 120,
        utv: null
    }
};

const serviceLabels = {
    exterior: 'Exterior Detail',
    interior: 'Interior Detail',
    ceramic: 'Ceramic Coatings & Polishing',
    polishing: 'Polishing',
    maintenance: 'Maintenance Detail In/Ex'
};

const vehicleLabels = {
    sedan: 'Coupe / Sedan',
    suv: 'SUV / Pickup Truck',
    large: 'Large Truck / Van',
    utv: 'UTV / ATV'
};

let calcState = {
    vehicle: { key: '', label: '' },
    service: { key: '', label: '', price: 0 },
    addons: []
};

// Gentle scroll helper — nudges the next step into view without jumping
function scrollToStep(stepId) {
    setTimeout(() => {
        const target = document.getElementById(stepId);
        if (target) {
            const rect = target.getBoundingClientRect();
            // Only scroll if the element isn't already mostly visible
            if (rect.top > window.innerHeight * 0.65) {
                window.scrollBy({ top: rect.top - window.innerHeight * 0.45, behavior: 'smooth' });
            }
        }
    }, 300);
}

function selectVehicle(el) {
    const key = el.getAttribute('data-key');
    const siblings = el.parentElement.querySelectorAll('.calc-option');
    siblings.forEach(s => s.classList.remove('selected'));
    el.classList.add('selected');
    
    calcState.vehicle = { key, label: vehicleLabels[key] };
    
    // Update service prices based on vehicle
    updateServicePrices();
    
    // If a service was already selected, re-select it to update price
    if (calcState.service.key) {
        const activeService = document.querySelector(`[data-key="${calcState.service.key}"][data-group="service"]`);
        if (activeService) {
            selectService(activeService, true);
        }
    }
    
    updateCalcSummary();
    
    // Auto-scroll to step 2
    scrollToStep('step-2');
}

function updateServicePrices() {
    const vehicleKey = calcState.vehicle.key;
    if (!vehicleKey) return;
    
    const serviceIds = ['exterior', 'interior', 'ceramic', 'polishing', 'maintenance'];
    serviceIds.forEach(svc => {
        const priceEl = document.getElementById('price-' + svc);
        const optionEl = document.querySelector(`[data-key="${svc}"][data-group="service"]`);
        const price = pricingMatrix[svc][vehicleKey];
        
        if (price === null) {
            priceEl.innerText = 'N/A';
            optionEl.classList.add('disabled-option');
            optionEl.style.opacity = '0.4';
            optionEl.style.pointerEvents = 'none';
        } else {
            priceEl.innerText = '$' + price;
            optionEl.classList.remove('disabled-option');
            optionEl.style.opacity = '1';
            optionEl.style.pointerEvents = 'auto';
        }
    });
}

function selectService(el, skipScroll) {
    const key = el.getAttribute('data-key');
    const vehicleKey = calcState.vehicle.key;
    
    if (!vehicleKey) {
        // Scroll back to step 1 instead of alert
        scrollToStep('step-1');
        return;
    }
    
    const price = pricingMatrix[key][vehicleKey];
    if (price === null) return;
    
    const siblings = el.parentElement.querySelectorAll('.calc-option');
    siblings.forEach(s => s.classList.remove('selected'));
    el.classList.add('selected');
    
    calcState.service = { key, label: serviceLabels[key], price };
    updateCalcSummary();
    
    // Auto-scroll to step 3 (add-ons)
    if (!skipScroll) {
        scrollToStep('step-3');
    }
}

function toggleAddon(el) {
    const val = parseInt(el.getAttribute('data-val'));
    const name = el.getAttribute('data-name');
    
    // Special handling for odor/stain removal
    if (name === 'Odor/Stain Removal') {
        const severityPanel = document.getElementById('odorSeverity');
        if (el.classList.contains('selected')) {
            el.classList.remove('selected');
            severityPanel.style.display = 'none';
            calcState.addons = calcState.addons.filter(a => a.name !== name);
        } else {
            el.classList.add('selected');
            severityPanel.style.display = 'block';
            // Default to light ($20)
            const defaultCost = 20;
            calcState.addons.push({ val: defaultCost, name });
        }
    } else {
        if (el.classList.contains('selected')) {
            el.classList.remove('selected');
            calcState.addons = calcState.addons.filter(a => a.name !== name);
        } else {
            el.classList.add('selected');
            calcState.addons.push({ val, name });
        }
    }
    updateCalcSummary();
}

function selectOdorSeverity(btn, event) {
    event.stopPropagation();
    const cost = parseInt(btn.getAttribute('data-cost'));
    
    // Update selected button style
    const allBtns = btn.parentElement.querySelectorAll('.severity-btn');
    allBtns.forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    
    // Update addon cost
    const addonIndex = calcState.addons.findIndex(a => a.name === 'Odor/Stain Removal');
    if (addonIndex !== -1) {
        calcState.addons[addonIndex].val = cost;
    }
    updateCalcSummary();
}

function updateCalcSummary() {
    let servicePrice = calcState.service.price || 0;
    let addonsTotal = 0;
    calcState.addons.forEach(a => addonsTotal += a.val);
    let total = servicePrice + addonsTotal;
    
    document.getElementById('calc-total').innerText = total;
    
    let breakdown = [];
    if (calcState.vehicle.label) breakdown.push(calcState.vehicle.label);
    if (calcState.service.label) breakdown.push(calcState.service.label + ' ($' + calcState.service.price + ')');
    if (calcState.addons.length > 0) {
        const addonNames = calcState.addons.map(a => a.name + ' (+$' + a.val + ')');
        breakdown.push(addonNames.join(', '));
    }
    
    document.getElementById('calc-breakdown').innerText = breakdown.join(' | ') || 'Select vehicle & service above';
    
    // Show/hide the Book Now actions
    const actionsPanel = document.getElementById('calcBookActions');
    if (calcState.service.key && calcState.vehicle.key) {
        actionsPanel.style.display = 'block';
    } else {
        actionsPanel.style.display = 'none';
    }
}

function sendQuoteEmail() {
    const vehicleLabel = calcState.vehicle.label || 'Not selected';
    const serviceLabel = calcState.service.label || 'Not selected';
    const addonsText = calcState.addons.length > 0
        ? calcState.addons.map(a => '• ' + a.name + ' — $' + a.val).join('\n')
        : 'None';
    const total = document.getElementById('calc-total')?.innerText || '0';
    
    const subject = encodeURIComponent('Quote Request — Mac\'s Signature Auto Care');
    const body = encodeURIComponent(
        'Hi Mac\'s Signature Auto Care,\n\n' +
        'I\'d like to request a quote for the following:\n\n' +
        '— Vehicle: ' + vehicleLabel + '\n' +
        '— Service: ' + serviceLabel + '\n' +
        '— Add-ons:\n' + addonsText + '\n\n' +
        '— Estimated Total: $' + total + '\n\n' +
        'Please let me know availability. Thank you!'
    );
    
    window.location.href = 'mailto:macdetailing25@gmail.com?subject=' + subject + '&body=' + body;
}


// Counter Logic
function startCounters() {
    const counters = document.querySelectorAll('.counter');
    const speed = 50; 

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        let count = 0;
        const inc = target / speed;

        const updateCount = () => {
            count += inc;
            if (count < target) {
                counter.innerText = Math.ceil(count);
                setTimeout(updateCount, 40);
            } else {
                counter.innerText = target;
            }
        };

        let observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    updateCount();
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });
        
        observer.observe(counter);
    });
}
document.addEventListener('DOMContentLoaded', startCounters);
// v2.1 - updated 2026-03-25
