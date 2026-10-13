
        // ---------- THEME TOGGLE ----------
        function toggleTheme() {
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            html.setAttribute('data-theme', next);
            
            // Update toggle icons
            const moon = document.querySelector('.fa-moon');
            const sun = document.querySelector('.fa-sun');
            if (next === 'dark') {
                moon?.classList.add('hidden');
                sun?.classList.remove('hidden');
            } else {
                moon?.classList.remove('hidden');
                sun?.classList.add('hidden');
            }
            
            // Save preference (optional)
            fetch('/toggle-theme/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).catch(() => {});
        }
        
        // Initialize theme icons on page load
        document.addEventListener('DOMContentLoaded', function() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme') || 'light';
            const moon = document.querySelector('.fa-moon');
            const sun = document.querySelector('.fa-sun');
            
            if (currentTheme === 'dark') {
                moon?.classList.add('hidden');
                sun?.classList.remove('hidden');
            } else {
                moon?.classList.remove('hidden');
                sun?.classList.add('hidden');
            }
        });
        
        function getCookie(name) {
            let value = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        value = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return value;
        }
        
        // ---------- MOBILE MENU ----------
        document.getElementById('mobile-menu-btn')?.addEventListener('click', function() {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        });
        
        // ---------- SMOOTH SCROLL ----------
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
        
        // ---------- SCROLL REVEAL (IntersectionObserver) ----------
        document.addEventListener('DOMContentLoaded', function() {
            const reveals = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
            
            reveals.forEach(el => observer.observe(el));
            
            // Skill bars (inside .skill-section)
            const skillSections = document.querySelectorAll('.skill-section');
            const skillObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const bars = entry.target.querySelectorAll('.skill-bar');
                        bars.forEach(bar => {
                            const width = bar.getAttribute('data-width');
                            bar.style.width = width + '%';
                        });
                    }
                });
            }, { threshold: 0.3 });
            
            skillSections.forEach(section => skillObserver.observe(section));
        });


