/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./gameProject/game1/**/*.{html,js}",
            // "./**/*.{html,js}"
  ],
  theme: {
    extend: {
      fontFamily:{
        //
      },
      colors: {
        "customGrey": "#b0babf",
        //
      },
    },
  },
  plugins: [
    require("tailwindcss"),
    require("autoprefixer"),
  ],
}