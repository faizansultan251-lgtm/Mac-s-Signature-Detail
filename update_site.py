import re
import os

html_file = 'index.html'
css_file = 'css/styles.css'
js_file = 'js/script.js'

with open(html_file, 'r') as f:
    html = f.read()

# Replace business name
html = html.replace('Next Level Detailing', "John's Car Detail")
html = html.replace('NEXT LEVEL<br><span class="text-glow">DETAILING</span>', 'JOHN\'S<br><span class="text-glow">CAR DETAIL</span>')
html = html.replace('NEXT LEVEL DETAILING', "JOHN'S CAR DETAIL")
html = html.replace('Next Level', "John's Car Detail")

# Hero background image
html = html.replace("url('assets/hero-bg-v2.png')", "url('assets/modern_hero_bg.png')")
html = html.replace("url('assets/hero-bg.png')", "url('assets/modern_hero_bg.png')")

# Gallery
html = html.replace('assets/exterior-wash.png', 'assets/showroom_exterior.png')
html = html.replace('assets/interior-glow.png', 'assets/showroom_interior.png')

# Emojis in features grid
html = html.replace('<div class="feature-icon">🏅</div>', '<div class="feature-icon"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Z"/><path d="m10.5 14.5-2.5 8 4-3 4 3-2.5-8"/></svg></div>')
html = html.replace('<div class="feature-icon">🔍</div>', '<div class="feature-icon"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg></div>')
html = html.replace('<div class="feature-icon">✨</div>', '<div class="feature-icon"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v18m9-9H3m14.1 6.1L4.9 4.9m14.2 0L4.9 19.1"/></svg></div>')

# Emojis in Trust Strip -> To be replaced with new Trust Strip
trust_strip_html = """
    <!-- 2) Trust / Value Strip -->
    <section id="trust-strip" class="trust-strip">
        <div class="trust-stat reveal-up">
            <h3 class="counter" data-target="2500">0</h3>
            <p>Cars Detailed</p>
        </div>
        <div class="trust-stat reveal-up" style="transition-delay: 100ms;">
            <h3 class="counter" data-target="500">0</h3>
            <p>5-Star Reviews</p>
        </div>
        <div class="trust-stat reveal-up" style="transition-delay: 200ms;">
            <h3 class="counter" data-target="99">0</h3><span>%</span>
            <p>Satisfaction</p>
        </div>
        <div class="trust-stat reveal-up" style="transition-delay: 300ms;">
            <h3 class="counter" data-target="10">0</h3><span>+</span>
            <p>Years Exp</p>
        </div>
    </section>
"""
import re
html = re.sub(r'<!-- 2\) Trust / Value Strip -->.*?<!-- 3\) Services', trust_strip_html + '\n    <!-- 3) Services', html, flags=re.DOTALL)

# Testimonials update
testimonials_html = """
    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials-section section-separator reveal-up cinematic-pacing">
        <h2 class="section-title text-center">Client <span class="text-glow">Reviews</span></h2>
        <div class="testimonials-container">
            <div class="testimonial-card featured-testimonial glossy-panel reveal-up">
                <div class="review-header">
                    <div class="stars">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </div>
                    <span class="verified"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Verified</span>
                </div>
                <p class="review-text">"Absolutely incredible service. My car looks better than the day I bought it off the lot. The gold package was worth every penny. Will never use another detailing service!"</p>
                <div class="reviewer-info">
                    <h4>Michael T.</h4>
                    <span>BMW M4 Owner</span>
                </div>
            </div>
            <div class="testimonials-grid">
                <div class="testimonial-card glossy-panel reveal-up" style="transition-delay: 100ms;">
                    <div class="stars">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </div>
                    <p>"John's Car Detail came right to my office. Super professional, fast, and the interior smells amazing."</p>
                    <h4>- Sarah K.</h4>
                </div>
                <div class="testimonial-card glossy-panel reveal-up" style="transition-delay: 200ms;">
                    <div class="stars">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                    </div>
                    <p>"The attention to detail is unmatched. Premium experience from start to finish."</p>
                    <h4>- David L.</h4>
                </div>
            </div>
        </div>
    </section>
"""
html = re.sub(r'<!-- Testimonials Section -->.*?<!-- 7\) Quick Quote', testimonials_html + '\n    <!-- 7) Quick Quote', html, flags=re.DOTALL)

# Instant Quote Calculator
calculator_html = """
    <!-- 4) Instant Quote Calculator -->
    <section id="comparison" class="comparison-section reveal-up cinematic-bg" style="background-image: url('assets/showroom_interior.png'); position: relative;">
        <div style="position: absolute; inset: 0; background: rgba(5,5,5,0.9); z-index: 1;"></div>
        <div class="quote-calculator-container glass-container" style="position: relative; z-index: 2; max-width: 800px; margin: 0 auto;">
            <h2 class="section-title text-center" style="margin-bottom: 1rem;">Instant Quote <span class="text-glow">Calculator</span></h2>
            <p class="text-center text-muted" style="margin-bottom: 2rem;">Build your custom detailing package and get an instant, transparent price.</p>
            
            <div class="calculator-steps">
                <!-- Step 1 -->
                <div class="calc-step active" id="step-1">
                    <h3>1. Select Vehicle Size</h3>
                    <div class="calc-options-grid">
                        <div class="calc-option" data-group="size" data-val="0" data-name="Sedan/Coupe" onclick="selectOption(this)">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 16H9m10 0h3v-3.15a1 1 0 0 0-.84-.99L16 11l-2.7-3.6a2 2 0 0 0-1.6-.8H9.3a2 2 0 0 0-1.6.8L5 11l-5.16.86a1 1 0 0 0-.84.99V16h3m10 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m-10 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0"/></svg>
                            <span>Sedan / Coupe</span>
                        </div>
                        <div class="calc-option" data-group="size" data-val="20" data-name="SUV/Truck" onclick="selectOption(this)">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="10" rx="2" ry="2"/><path d="M22 11h-2v4h2v-4zM2 11h2v4H2v-4zM6 17v2M18 17v2"/></svg>
                            <span>SUV / Truck (+ $20)</span>
                        </div>
                    </div>
                </div>
                
                <!-- Step 2 -->
                <div class="calc-step mt-2" id="step-2">
                    <h3>2. Select Base Package</h3>
                    <div class="calc-options-grid">
                        <div class="calc-option" data-group="package" data-val="120" data-name="Basic Interior" onclick="selectOption(this)">
                            <h4>Basic Interior</h4>
                            <span class="price">$120</span>
                        </div>
                        <div class="calc-option" data-group="package" data-val="80" data-name="Basic Exterior" onclick="selectOption(this)">
                            <h4>Basic Exterior</h4>
                            <span class="price">$80</span>
                        </div>
                        <div class="calc-option recommended" data-group="package" data-val="200" data-name="Gold Package" onclick="selectOption(this)">
                            <div class="featured-tag">Popular</div>
                            <h4>Gold Package</h4>
                            <span class="price">$200</span>
                        </div>
                        <div class="calc-option" data-group="package" data-val="220" data-name="Premium Finish" onclick="selectOption(this)">
                            <h4>Premium Finish</h4>
                            <span class="price">$220</span>
                        </div>
                    </div>
                </div>
                
                <!-- Step 3 -->
                <div class="calc-step mt-2" id="step-3">
                    <h3>3. Select Add-ons</h3>
                    <div class="calc-options-grid">
                        <div class="calc-option addon" data-group="addon" data-val="30" data-name="Carpet Shampoo" onclick="toggleAddon(this)">
                            <h4>Carpet Shampoo</h4>
                            <span class="price">+ $30</span>
                        </div>
                        <div class="calc-option addon" data-group="addon" data-val="35" data-name="Pet Hair Removal" onclick="toggleAddon(this)">
                            <h4>Pet Hair Removal</h4>
                            <span class="price">+ $35</span>
                        </div>
                        <div class="calc-option addon" data-group="addon" data-val="50" data-name="Engine Bay Detailing" onclick="toggleAddon(this)">
                            <h4>Engine Bay Detailing</h4>
                            <span class="price">+ $50</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="calc-summary mt-2 neon-edge">
                <div class="summary-details">
                    <h4>Total Estimate</h4>
                    <p id="calc-breakdown">Select options above</p>
                </div>
                <div class="summary-total">
                    $<span id="calc-total">0</span>
                </div>
            </div>
            <button class="btn btn-primary w-100 mt-2 pulse-effect calc-book-btn" onclick="document.getElementById('booking').scrollIntoView();" disabled>Book This Package</button>
        </div>
    </section>
"""
html = re.sub(r'<!-- 4\) Visual Comparison Section -->.*?<!-- 5\) Why Choose', calculator_html + '\n    <!-- 5) Why Choose', html, flags=re.DOTALL)

with open(html_file, 'w') as f:
    f.write(html)

with open(css_file, 'r') as f:
    css = f.read()

# Update colors
css = css.replace('--bg-dark: #050505;', '--bg-dark: #000000;')
css = css.replace('--surface-dark: #0a0a0a;', '--surface-dark: #111111;')
css = css.replace('--surface-light: #151515;', '--surface-light: #1a1a1a;')
css = css.replace('--accent-red: #FF6A00;', '--accent-red: #003BFF; /* Deep Electric Blue */')
css = css.replace('--accent-orange: #FFB300;', '--accent-orange: #007BFF; /* Bright Blue */')
css = css.replace('--accent-blue: #00E5FF;', '--accent-blue: #C0C0C0; /* Silver Accent */')

css = css.replace('rgba(255, 106, 0,', 'rgba(0, 59, 255,')
css = css.replace('rgba(255, 179, 0,', 'rgba(0, 123, 255,')
css = css.replace('rgba(0, 229, 255,', 'rgba(192, 192, 192,')
css = css.replace('rgba(230, 46, 0,', 'rgba(0, 90, 255,')

# Add trust strip CSS & Calculator CSS
extra_css = """

/* === Trust Strip / Counters === */
.trust-strip {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    background: linear-gradient(90deg, #050505, #151515, #050505);
    padding: 40px 5%;
    border-top: 1px solid rgba(192,192,192,0.1);
    border-bottom: 2px solid var(--accent-orange);
    gap: 30px;
}

.trust-stat {
    text-align: center;
    color: white;
}

.trust-stat h3 {
    font-size: 3rem;
    font-weight: 900;
    color: var(--accent-orange);
    text-shadow: var(--glow-orange);
    display: inline-block;
    margin-bottom: 5px;
}

.trust-stat span {
    font-size: 2rem;
    font-weight: 900;
    color: var(--accent-orange);
}

.trust-stat p {
    font-size: 1.1rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* === Testimonials Upgrade === */
.testimonials-container {
    display: flex;
    flex-direction: column;
    gap: 30px;
    max-width: 1000px;
    margin: 0 auto;
}

.featured-testimonial {
    background: linear-gradient(135deg, rgba(0, 59, 255, 0.1), rgba(10, 10, 10, 0.95)) !important;
    border: 1px solid var(--accent-orange) !important;
    padding: 50px 40px !important;
    text-align: center;
    transform: scale(1.02);
}

.featured-testimonial .review-text {
    font-size: 1.4rem !important;
    line-height: 1.6;
    margin: 30px 0;
    color: white;
}

.review-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.verified {
    display: flex;
    align-items: center;
    gap: 5px;
    color: #4CAF50;
    font-weight: 600;
    font-size: 0.9rem;
}

.reviewer-info h4 {
    font-size: 1.3rem;
    margin-bottom: 5px;
}

.reviewer-info span {
    color: var(--text-muted);
    font-size: 0.95rem;
}

/* === Quote Calculator === */
.quote-calculator-container {
    padding: 40px;
}

.calc-step {
    margin-bottom: 30px;
}
.calc-step h3 {
    margin-bottom: 15px;
    font-size: 1.3rem;
    color: var(--accent-blue);
}
.calc-options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
}

.calc-option {
    background: rgba(20,20,20,0.8);
    border: 2px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
    position: relative;
    overflow: hidden;
}

.calc-option:hover {
    border-color: rgba(192,192,192,0.4);
    background: rgba(30,30,30,0.8);
}

.calc-option.selected {
    border-color: var(--accent-orange);
    background: rgba(0, 123, 255, 0.15);
    box-shadow: 0 0 20px rgba(0, 123, 255, 0.3);
}

.calc-option svg {
    color: var(--accent-blue);
    margin-bottom: 5px;
}

.calc-option.selected svg {
    color: var(--accent-orange);
}

.calc-option.recommended {
    border-color: rgba(0, 123, 255, 0.5);
}

.featured-tag {
    position: absolute;
    top: 0;
    right: 0;
    background: var(--accent-orange);
    color: white;
    font-size: 0.7rem;
    padding: 3px 8px;
    border-bottom-left-radius: 8px;
    font-weight: bold;
}

.calc-option .price {
    font-weight: bold;
    color: var(--text-muted);
}
.calc-option.selected .price {
    color: white;
}

.calc-summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    background: rgba(0,0,0,0.6);
    border-radius: 10px;
    margin-top: 30px;
}

.summary-details h4 {
    margin-bottom: 5px;
}
.summary-details p {
    color: var(--accent-blue);
    font-size: 0.95rem;
}

.summary-total {
    font-size: 2.5rem;
    font-family: var(--font-heading);
    font-weight: 800;
    color: var(--accent-orange);
    text-shadow: var(--glow-orange);
}
"""

css += extra_css
with open(css_file, 'w') as f:
    f.write(css)

# Update JS logic for calculator and counters
with open(js_file, 'r') as f:
    js = f.read()

calc_js = """
// Quote Calculator Logic
let calcState = {
    size: { val: 0, name: '' },
    package: { val: 0, name: '' },
    addons: []
};

function selectOption(el) {
    let group = el.getAttribute('data-group');
    let val = parseInt(el.getAttribute('data-val'));
    let name = el.getAttribute('data-name');
    
    // Remove selected from siblings
    let siblings = el.parentElement.querySelectorAll('.calc-option');
    siblings.forEach(s => s.classList.remove('selected'));
    
    el.classList.add('selected');
    calcState[group] = { val, name };
    updateSummary();
}

function toggleAddon(el) {
    let val = parseInt(el.getAttribute('data-val'));
    let name = el.getAttribute('data-name');
    
    if (el.classList.contains('selected')) {
        el.classList.remove('selected');
        calcState.addons = calcState.addons.filter(a => a.name !== name);
    } else {
        el.classList.add('selected');
        calcState.addons.push({ val, name });
    }
    updateSummary();
}

function updateSummary() {
    let total = calcState.size.val + calcState.package.val;
    calcState.addons.forEach(a => total += a.val);
    
    document.getElementById('calc-total').innerText = total;
    
    let breakdown = [];
    if (calcState.package.name) breakdown.push(calcState.package.name);
    if (calcState.size.name && calcState.size.val > 0) breakdown.push('SUV/Truck (+20)');
    if (calcState.addons.length > 0) breakdown.push('+' + calcState.addons.length + ' Add-ons');
    
    let bkText = breakdown.join(' | ');
    document.getElementById('calc-breakdown').innerText = bkText || 'Select options above';
    
    let bookBtn = document.querySelector('.calc-book-btn');
    if (calcState.package.name) {
        bookBtn.removeAttribute('disabled');
        // sync to actual contact form
        let select = document.getElementById('serviceSelect');
        if(select) {
           for(let i=0; i<select.options.length; i++) {
               if(select.options[i].text.includes(calcState.package.name)) {
                   select.selectedIndex = i;
                   break;
               }
           }
        }
    }
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

"""

js += "\n" + calc_js

with open(js_file, 'w') as f:
    f.write(js)

print("Update complete")
