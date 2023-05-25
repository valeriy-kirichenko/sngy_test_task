export default defineNuxtConfig({
    modules: ['@nuxtjs/apollo'],
    apollo: {
        clients: {
          default: {
            httpEndpoint: 'http://127.0.0.1:8000/api/'
          }
        },
      },
    css: [
        "vuetify/lib/styles/main.sass",
        "@mdi/font/css/materialdesignicons.css"
    ],
    build: {
        transpile: ["vuetify"]
    },
})
