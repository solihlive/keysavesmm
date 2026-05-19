import streamlit as st

# Streamlit sahifa sozlamalari (Sayt responsiv bo'lishi va keng yoyilishi uchun)
st.set_page_config(
    page_title="KeySave — SMM Bot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit paddinglarini olib tashlash (To'liq ekran qoplashi uchun)
st.markdown("""
    <style>
        .reportview-container .main .block-container{ padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem; }
        .main .block-container { padding: 0; max-width: 100%; }
        header {display: none !important;}
        footer {display: none !important;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Mukammallashtirilgan to'liq HTML + Tailwind + AOS Animatsiyali kod
html_code = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="keywords" content="Smm panel russian and uzbekistan,smm panel script,smm panel promotion">
  <title>KeySave — SMM Bot</title>

  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind = window.tailwind || {};
    tailwind.config = {
      theme: {
        extend: {
          colors: { neonCyan: '#00F0FF', neonPurple: '#8A2BE2' },
          fontFamily: { inter: ['Inter', 'sans-serif'] },
          keyframes: {
            float1: {
              '0%': { transform: 'translate3d(-10%, -10%, 0) scale(1)' },
              '50%': { transform: 'translate3d(5%, 10%, 0) scale(1.05)' },
              '100%': { transform: 'translate3d(-10%, -10%, 0) scale(1)' },
            },
            float2: {
              '0%': { transform: 'translate3d(10%, 5%, 0) scale(1)' },
              '50%': { transform: 'translate3d(-5%, -10%, 0) scale(1.06)' },
              '100%': { transform: 'translate3d(10%, 5%, 0) scale(1)' },
            },
            glow: {
              '0%': { boxShadow: '0 0 20px rgba(0,240,255,0.14), 0 0 40px rgba(138,43,226,0.08)' },
              '50%': { boxShadow: '0 0 30px rgba(0,240,255,0.18), 0 0 60px rgba(138,43,226,0.12)' },
              '100%': { boxShadow: '0 0 20px rgba(0,240,255,0.14), 0 0 40px rgba(138,43,226,0.08)' },
            }
          },
          animation: {
            float1: 'float1 10s ease-in-out infinite',
            float2: 'float2 12s ease-in-out infinite',
            glow: 'glow 3s ease-in-out infinite',
          },
        }
      }
    }
  </script>

  <style>
    :root { color-scheme: dark; }
    body { font-family: Inter, system-ui, -apple-system, sans-serif; background-color: #0b1329; overflow-x: hidden; }
    .neon-heading {
      text-shadow: 0 0 8px rgba(0,240,255,0.18), 0 0 20px rgba(138,43,226,0.10), 0 0 32px rgba(0,240,255,0.06);
    }
    .glass {
      background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));
      border: 1px solid rgba(255,255,255,0.06);
      backdrop-filter: blur(10px);
      transition: all 0.3s ease;
    }
    .glass:hover {
      border-color: rgba(0,240,255,0.3);
      transform: translateY(-2px);
    }
    .mesh { position: absolute; inset: 0; z-index: -50; overflow: hidden; pointer-events: none; }
    .mesh .blob { position: absolute; filter: blur(80px); opacity: 0.7; mix-blend-mode: screen; }
    .stat-num { font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }
    .lang-btn[data-active="true"] {
      background: linear-gradient(90deg, rgba(0,240,255,0.2), rgba(138,43,226,0.15));
      border-radius: 8px;
      padding: 4px 8px;
      color: #E6FEFF;
      font-weight: 600;
    }
  </style>
</head>
<body class="antialiased text-gray-100 relative">

  <div class="mesh" aria-hidden="true">
    <div class="blob w-[40rem] h-[40rem] rounded-full bg-gradient-to-r from-neonCyan/40 to-neonPurple/30 left-[-10%] top-[-10%] animate-float1"></div>
    <div class="blob w-[50rem] h-[50rem] rounded-full bg-gradient-to-r from-neonPurple/40 to-neonCyan/20 right-[-10%] bottom-[-10%] animate-float2"></div>
  </div>

  <header class="pt-8 pb-6 px-6 sm:px-8 lg:px-12">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <a href="#" class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-lg flex items-center justify-center bg-gradient-to-br from-neonCyan to-neonPurple">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
            <path d="M4 12c0-4.418 3.582-8 8-8 1.657 0 3.18.43 4.5 1.18L20 3l-1.5 3.5C19.57 8.82 20 10.343 20 12c0 4.418-3.582 8-8 8s-8-3.582-8-8z" fill="white" opacity="0.9"/>
            <path d="M8 12a4 4 0 0 1 8 0" stroke="#0ff" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <span class="text-lg font-semibold tracking-wide">KeySave</span>
      </a>

      <nav class="hidden md:flex items-center gap-6 text-sm text-gray-300">
        <a href="#features" data-i18n="nav.features" class="hover:text-white transition">Features</a>
        <a href="#stats" data-i18n="nav.stats" class="hover:text-white transition">Stats</a>
        <a href="#pricing" data-i18n="nav.pricing" class="hover:text-white transition">Pricing</a>
        <a href="https://t.me/KeySaveSMM_Bot" class="ml-2 inline-flex items-center gap-2 px-4 py-2 rounded-lg glass text-neonCyan" target="_blank" data-i18n="nav.openBot">Open Bot</a>
      </nav>

      <div class="flex items-center gap-3">
        <div class="flex items-center gap-2 text-sm">
          <button class="lang-btn text-gray-300 cursor-pointer" data-lang="en">EN</button>
          <button class="lang-btn text-gray-300 cursor-pointer" data-lang="ru">RU</button>
          <button class="lang-btn text-gray-300 cursor-pointer" data-lang="uz">UZ</button>
        </div>
      </div>
    </div>
  </header>

  <main class="px-6 sm:px-8 lg:px-12">
    <section class="relative z-10 my-10">
      <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
        <div data-aos="fade-right" data-aos-duration="1000">
          <p class="inline-flex items-center gap-2 text-sm text-neonCyan/80 font-medium mb-4" data-i18n="hero.tagline">Trusted SMM Automation</p>
          <h1 class="text-4xl sm:text-5xl md:text-6xl font-extrabold leading-tight neon-heading" data-i18n="hero.title">KeySave — SMM Bot for Rapid Growth</h1>
          <p class="mt-6 text-gray-300 max-w-xl" data-i18n="hero.desc">Fast, secure and scalable SMM services delivered through an automated Telegram bot...</p>

          <div class="mt-8 flex flex-col sm:flex-row gap-4">
            <a href="https://t.me/KeySaveSMM_Bot" class="inline-flex items-center justify-center gap-3 px-6 py-3 rounded-lg bg-gradient-to-r from-neonCyan to-neonPurple text-gray-900 font-semibold shadow-lg hover:scale-[1.05] transition transform animate-glow" target="_blank" data-i18n="hero.launchBot">Launch Bot</a>
            <a href="#features" class="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-lg glass text-gray-100/90" data-i18n="hero.learnFeatures">Learn features</a>
          </div>

          <div class="mt-8 grid grid-cols-2 sm:grid-cols-3 gap-3 max-w-md">
            <div class="glass px-4 py-3 rounded-lg flex items-center gap-3">
              <div class="text-neonCyan">⚡</div>
              <div>
                <div class="text-xs text-gray-400" data-i18n="mini.avgDelivery.label">Avg. Delivery</div>
                <div class="text-sm font-medium" data-i18n="mini.avgDelivery.value">~ 3–15 min</div>
              </div>
            </div>
            <div class="glass px-4 py-3 rounded-lg flex items-center gap-3">
              <div class="text-neonPurple">🛡️</div>
              <div>
                <div class="text-xs text-gray-400" data-i18n="mini.uptime.label">Uptime</div>
                <div class="text-sm font-medium" data-i18n="mini.uptime.value">99.9%</div>
              </div>
            </div>
            <div class="glass px-4 py-3 rounded-lg flex items-center gap-3">
              <div class="text-white">✨</div>
              <div>
                <div class="text-xs text-gray-400" data-i18n="mini.support.label">24/7</div>
                <div class="text-sm font-medium" data-i18n="mini.support.value">Support</div>
              </div>
            </div>
          </div>
        </div>

        <div data-aos="fade-left" data-aos-duration="1000" class="relative">
          <div class="glass rounded-2xl p-6 sm:p-8 border border-white/6 shadow-neon">
            <div class="flex items-center justify-between">
              <div>
                <div class="text-sm text-gray-400" data-i18n="connected.label">Connected Bot</div>
                <div class="text-lg font-semibold" data-i18n="connected.name">KeySave Bot</div>
              </div>
              <div class="text-sm text-gray-400" data-i18n="connected.version">v1.2.8</div>
            </div>
            <div class="mt-6">
              <div class="text-xs text-gray-400" data-i18n="recent.label">Recent orders</div>
              <ul class="mt-3 space-y-3">
                <li class="flex items-center justify-between border-b border-white/5 pb-2">
                  <div>
                    <div class="text-sm font-medium text-neonCyan" data-i18n="recent.item1.title">Instagram Likes</div>
                    <div class="text-xs text-gray-400" data-i18n="recent.item1.meta">@client_pro • 15 min ago</div>
                  </div>
                  <div class="text-sm font-bold text-white">+1.2k</div>
                </li>
                <li class="flex items-center justify-between">
                  <div>
                    <div class="text-sm font-medium text-neonPurple" data-i18n="recent.item2.title">Telegram Members</div>
                    <div class="text-xs text-gray-400" data-i18n="recent.item2.meta">@growing_channel • 45 min ago</div>
                  </div>
                  <div class="text-sm font-bold text-white">+850</div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="stats" class="mt-20" data-aos="fade-up" data-aos-duration="1000">
      <div class="max-w-7xl mx-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="glass rounded-xl p-6 text-center sm:text-left">
            <div class="text-sm text-gray-400" data-i18n="stats.activeUsers.label">Active Users</div>
            <div class="mt-3 text-4xl font-bold stat-num text-neonCyan" data-target="23540">0</div>
            <div class="mt-2 text-xs text-gray-400" data-i18n="stats.activeUsers.desc">Real users using KeySave daily</div>
          </div>
          <div class="glass rounded-xl p-6 text-center sm:text-left">
            <div class="text-sm text-gray-400" data-i18n="stats.services.label">Services Offered</div>
            <div class="mt-3 text-4xl font-bold stat-num text-neonPurple" data-target="110">0</div>
            <div class="mt-2 text-xs text-gray-400" data-i18n="stats.services.desc">Tiers & categories available</div>
          </div>
          <div class="glass rounded-xl p-6 text-center sm:text-left">
            <div class="text-sm text-gray-400" data-i18n="stats.orders.label">Completed Orders</div>
            <div class="mt-3 text-4xl font-bold stat-num text-white" data-target="768300">0</div>
            <div class="mt-2 text-xs text-gray-400" data-i18n="stats.orders.desc">Orders processed successfully</div>
          </div>
        </div>
      </div>
    </section>

    <section id="features" class="mt-24 pb-20">
      <div class="max-w-7xl mx-auto">
        <div class="text-center mb-12" data-aos="zoom-in">
          <h2 class="text-3xl font-extrabold text-white" data-i18n="features.title">Features built for scale</h2>
          <p class="mt-2 text-gray-400 max-w-2xl mx-auto" data-i18n="features.desc">Speed, security and support—everything you need to grow social accounts reliably.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="glass p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="100">
            <div class="text-neonCyan text-2xl mb-2">⚡</div>
            <div class="text-lg font-semibold" data-i18n="features.speed.title">Speed</div>
            <p class="mt-1 text-sm text-gray-400" data-i18n="features.speed.desc">Fast queue processing and parallel execution.</p>
          </div>
          <div class="glass p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="200">
            <div class="text-neonPurple text-2xl mb-2">🔒</div>
            <div class="text-lg font-semibold" data-i18n="features.security.title">Security</div>
            <p class="mt-1 text-sm text-gray-400" data-i18n="features.security.desc">Encrypted data handling and safe payment flows.</p>
          </div>
          <div class="glass p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="300">
            <div class="text-white text-2xl mb-2">🤝</div>
            <div class="text-lg font-semibold" data-i18n="features.support.title">Support</div>
            <p class="mt-1 text-sm text-gray-400" data-i18n="features.support.desc">24/7 support and live status updates.</p>
          </div>
          <div class="glass p-6 rounded-2xl" data-aos="fade-up" data-aos-delay="400">
            <div class="bg-gradient-to-r from-neonCyan to-neonPurple text-transparent bg-clip-text text-2xl mb-2">💎</div>
            <div class="text-lg font-semibold" data-i18n="features.pricing.title">Pricing</div>
            <p class="mt-1 text-sm text-gray-400" data-i18n="features.pricing.desc">Transparent pricing and bulk discounts.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="mb-20" data-aos="flip-up" data-aos-duration="1000">
      <div class="max-w-7xl mx-auto">
        <div class="glass rounded-2xl p-8 flex flex-col sm:flex-row items-center justify-between gap-6">
          <div>
            <div class="text-xl font-bold text-white" data-i18n="cta.title">Ready to automate your SMM workflows?</div>
            <div class="text-sm text-gray-400 mt-1" data-i18n="cta.desc">Connect KeySave bot and start scaling campaigns in minutes.</div>
          </div>
          <div class="flex items-center gap-3 w-full sm:w-auto justify-end">
            <a href="https://t.me/KeySaveBot" target="_blank" class="px-6 py-3 rounded-lg bg-neonCyan text-gray-900 font-bold text-center hover:scale-105 transition w-full sm:w-auto" data-i18n="cta.openBot">Open Bot</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="pb-10 text-center text-sm text-gray-500">
    © <span id="year"></span> <span data-i18n="footer.copy">KeySave. All rights reserved.</span>
  </footer>

  <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
  <script>
    AOS.init({ once: true });

    const translations = {
      en: {
        "nav.features": "Features", "nav.stats": "Stats", "nav.pricing": "Pricing", "nav.openBot": "Open Bot",
        "hero.tagline": "Trusted SMM Automation", "hero.title": "KeySave — SMM Bot for Rapid Growth",
        "hero.desc": "Fast, secure and scalable SMM services delivered through an automated Telegram bot. Save time, scale campaigns, and keep control with bank-grade security and round-the-clock support.",
        "hero.launchBot": "Launch Bot", "hero.learnFeatures": "Learn features",
        "mini.avgDelivery.label": "Avg. Delivery", "mini.avgDelivery.value": "~ 3–15 min",
        "mini.uptime.label": "Uptime", "mini.uptime.value": "99.9%", "mini.support.label": "24/7", "mini.support.value": "Support",
        "connected.label": "Connected Bot", "connected.name": "KeySave Bot", "connected.version": "v1.2.8",
        "recent.label": "Recent orders", "recent.item1.title": "Instagram Likes", "recent.item1.meta": "@client_pro • 15 min ago",
        "recent.item2.title": "Telegram Members", "recent.item2.meta": "@growing_channel • 45 min ago",
        "features.title": "Features built for scale", "features.desc": "Speed, security and support—everything you need to grow social accounts reliably.",
        "features.speed.title": "Speed", "features.speed.desc": "Fast queue processing and parallel execution — deliver results quickly.",
        "features.security.title": "Security", "features.security.desc": "Encrypted data handling, role-based access, and safe payment flows.",
        "features.support.title": "Support", "features.support.desc": "24/7 support and live status updates for mission-critical campaigns.",
        "features.pricing.title": "Pricing", "features.pricing.desc": "Transparent pricing and bulk discounts.",
        "cta.title": "Ready to automate your SMM workflows?", "cta.desc": "Connect KeySave bot and start scaling campaigns in minutes.",
        "cta.openBot": "Open KeySave Bot", "footer.copy": "KeySave. All rights reserved."
      },
      ru: {
        "nav.features": "Функции", "nav.stats": "Статистика", "nav.pricing": "Тарифы", "nav.openBot": "Открыть бота",
        "hero.tagline": "Надёжная SMM-автоматизация", "hero.title": "KeySave — SMM-бот для быстрого роста",
        "hero.desc": "Быстрые, безопасные и масштабируемые SMM-услуги через Telegram-бота. Экономьте время, масштабируйте кампании и сохраняйте контроль.",
        "hero.launchBot": "Запустить бота", "hero.learnFeatures": "Подробнее",
        "mini.avgDelivery.label": "Среднее время", "mini.avgDelivery.value": "~ 3–15 мин",
        "mini.uptime.label": "Аптайм", "mini.uptime.value": "99.9%", "mini.support.label": "24/7", "mini.support.value": "Поддержка",
        "connected.label": "Подключённый бот", "connected.name": "KeySave Bot", "connected.version": "v1.2.8",
        "recent.label": "Последние заказы", "recent.item1.title": "Лайки в Instagram", "recent.item1.meta": "@client_pro • 15 мин назад",
        "recent.item2.title": "Подписчики в Telegram", "recent.item2.meta": "@growing_channel • 45 мин назад",
        "features.title": "Функции для масштабирования", "features.desc": "Скорость, безопасность и поддержка — всё, что нужно для роста соц-сетей.",
        "features.speed.title": "Скорость", "features.speed.desc": "Быстрая обработка и параллельное выполнение.",
        "features.security.title": "Безопасность", "features.security.desc": "Шифрование данных и безопасные платежи.",
        "features.support.title": "Поддержка", "features.support.desc": "Круглосуточная поддержка и обновления статуса.",
        "features.pricing.title": "Тарифы", "features.pricing.desc": "Прозрачные цены и скидки при больших объёмах.",
        "cta.title": "Готовы автоматизировать SMM-процессы?", "cta.desc": "Подключите KeySave бота и начните масштабировать кампании.",
        "cta.openBot": "Открыть KeySave бота", "footer.copy": "KeySave. Все права защищены."
      },
      uz: {
        "nav.features": "Xususiyatlar", "nav.stats": "Statistika", "nav.pricing": "Narxlar", "nav.openBot": "Botni ochish",
        "hero.tagline": "Ishonchli SMM avtomatlashtirish", "hero.title": "KeySave — tez o‘sish uchun SMM-bot",
        "hero.desc": "Tez, xavfsiz va kengaytiriladigan SMM xizmatlari Telegram-bot orqali. Vaqtni tejang, kampaniyalarni kattalashtiring va bank darajasidagi xavfsizlik bilan nazorat qiling.",
        "hero.launchBot": "Botni ishga tushur", "hero.learnFeatures": "Xususiyatlarga qarang",
        "mini.avgDelivery.label": "O'rtacha yetkazish", "mini.avgDelivery.value": "~ 3–15 min",
        "mini.uptime.label": "Ish vaqti", "mini.uptime.value": "99.9%", "mini.support.label": "24/7", "mini.support.value": "Qo'llab-quvvatlash",
        "connected.label": "Ulangan bot", "connected.name": "KeySave Bot", "connected.version": "v1.2.8",
        "recent.label": "So'nggi buyurtmalar", "recent.item1.title": "Instagram layklar", "recent.item1.meta": "@client_pro • 15 daqiqa oldin",
        "recent.item2.title": "Telegram a'zolari", "recent.item2.meta": "@growing_channel • 45 daqiqa oldin",
        "features.title": "Masshtablash uchun xususiyatlar", "features.desc": "Tezlik, xavfsizlik va yordam — ijtimoiy hisoblarni ishonchli o'stirish uchun.",
        "features.speed.title": "Tezlik", "features.speed.desc": "Tez navbat va parallel bajarish — natijani tez etkazing.",
        "features.security.title": "Xavfsizlik", "features.security.desc": "Ma'lumotlarni shifrlash, rollarga asoslangan kirish va xavfsiz to'lovlar.",
        "features.support.title": "Qo'llab-quvvatlash", "features.support.desc": "24/7 yordam va holat yangilanishlari.",
        "features.pricing.title": "Narxlar", "features.pricing.desc": "Aniq narxlar va ko'lam chegirmalari.",
        "cta.title": "SMM jarayonlaringizni avtomatlashtirishga tayyormisiz?", "cta.desc": "KeySave botini ulab, kampaniyalarni daqiqalarda kattalashtiring.",
        "cta.openBot": "KeySave botini ochish", "footer.copy": "KeySave. Barcha huquqlar himoyalangan."
      }
    };

    function applyTranslations(lang) {
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const txt = translations[lang] ? translations[lang][key] : null;
        if (txt) el.textContent = txt;
      });
      document.documentElement.lang = lang;
    }

    const langButtons = document.querySelectorAll('.lang-btn');
    function setLanguage(lang) {
      applyTranslations(lang);
      langButtons.forEach(btn => btn.dataset.active = btn.getAttribute('data-lang') === lang ? 'true' : 'false');
    }

    langButtons.forEach(btn => {
      btn.addEventListener('click', () => setLanguage(btn.getAttribute('data-lang')));
    });

    setLanguage('en');
    document.getElementById('year').textContent = new Date().getFullYear();

    // Silliq sanaydigan Counter Animatsiyasi
    const counters = document.querySelectorAll('.stat-num');
    const io = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-target'), 10);
          let current = 0;
          const step = Math.ceil(target / 100);
          const timer = setInterval(() => {
            current += step;
            if (current >= target) {
              el.textContent = target.toLocaleString();
              clearInterval(timer);
            } else {
              el.textContent = current.toLocaleString();
            }
          }, 20);
          io.unobserve(el);
        }
      });
    }, { threshold: 0.5 });
    counters.forEach(c => io.observe(c));
  </script>
</body>
</html>
"""

# HTML kodini Streamlit sahifasiga xatosiz va to'liq yuklash (Balandligi moslashuvchan)
st.components.v1.html(html_code, height=1800, scrolling=True)
