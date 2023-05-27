import { createVuetify } from "vuetify"
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import * as labsComponents from 'vuetify/labs/components'
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

export default defineNuxtPlugin(nuxtApp => {
    const vuetify = createVuetify({
        ssr: true,
        components: {
            ...components,
            ...labsComponents,
            ...directives,
          },
    })
    nuxtApp.vueApp.use(vuetify)
  })
