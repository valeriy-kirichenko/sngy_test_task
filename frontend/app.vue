<template>
  <div>
    <TheHeader @search="fetchSearch" @showFired="fetchShowFired" :selected="selected" />
    <DataTable @selected="fetchSelected" :search="search" :fired="showFired" />
  </div>
</template>

<script>
    import { ref } from 'vue'

    export default {
        setup() {
            const search = ref('')
            const selected = ref([])
            const showFired = ref()
            const fetchSearch = (event) => {
                search.value = event
            }

            const fetchSelected = (event) => {
                selected.value = event
            }

            const fetchShowFired = (event) => {
                showFired.value = event
            }

            return {
                search,
                selected,
                showFired,
                fetchSearch,
                fetchSelected,
                fetchShowFired
            }
        }
    }
</script>