<template>
  <div>
    <TheHeader @search="fetchSearch" :selected="selected" />
    <DataTable @selected="fetchSelected" :search="search" />
  </div>
</template>

<script>
    import { ref } from 'vue'

    export default {
        setup() {
            const search = ref('')
            const selected = ref([])
            const fetchSearch = (event) => {
                search.value = event
            }

            const fetchSelected = (event) => {
                selected.value = event
            }

            return {
                search,
                selected,
                fetchSearch,
                fetchSelected
            }
        }
    }
</script>