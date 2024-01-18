/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      fontFamily: {
        palanquin: ["Palanquin", "sans-serif"],
        montserrat: ["Montserrat", "sans-serif"],
        opensans: ["Open Sans", "sans-serif"],
        playfair: ["Playfair Display", "sans-serif"],
      },
      screens: {
        xs:"480px",
        ss: "620px",
        sm: "768px",
        md: "1060px",
        wide: "1440px",
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
