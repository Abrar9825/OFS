module.exports = {
  // content: ["./pages/*.{html,js}", "./index.html", "./*.html", "./js/*.js"],
  theme: {
    extend: {
      colors: {
        // Primary Colors
        primary: "#0a0a4d", // Oxford Blue
        secondary: "#1e3a8a", // blue-800
        accent: "#10b981", // emerald-500
        
        // Background Colors
        background: "#ffffff", // white
        surface: "#f8fafc", // slate-50
        
        // Text Colors
        'text-primary': "#1f2937", // gray-800
        'text-secondary': "#6b7280", // gray-500
        
        // Status Colors
        success: "#059669", // emerald-600
        warning: "#f59e0b", // amber-500
        error: "#dc2626", // red-600
        
        // Custom Oxford Blue variations
        oxford: {
          50: "#f0f0ff",
          100: "#e0e0ff",
          200: "#c7c7ff",
          300: "#a5a5ff",
          400: "#8080ff",
          500: "#5c5cff",
          600: "#4040ff",
          700: "#2e2eff",
          800: "#1e1eff",
          900: "#0a0a4d",
          950: "#050528"
        },
        
        // Glass effect colors
        glass: {
          border: "rgba(255, 255, 255, 0.2)",
          bg: "rgba(255, 255, 255, 0.1)"
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        inter: ['Inter', 'sans-serif'],
        jetbrains: ['JetBrains Mono', 'monospace']
      },
      fontWeight: {
        normal: '400',
        medium: '500',
        semibold: '600',
        bold: '700'
      },
      boxShadow: {
        'glass': '0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'glass-hover': '0 20px 40px -10px rgba(10, 10, 77, 0.3)',
        'cta': '0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
        'cta-hover': '0 20px 40px -10px rgba(10, 10, 77, 0.3)'
      },
      backdropBlur: {
        'glass': '10px'
      },
      transitionDuration: {
        '250': '250ms'
      },
      transitionTimingFunction: {
        'ease-in-out': 'ease-in-out'
      },
      scale: {
        '102': '1.02'
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-in-out',
        'pulse-slow': 'pulse 3s infinite'
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' }
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' }
        }
      }
    },
  },
  plugins: [],
}