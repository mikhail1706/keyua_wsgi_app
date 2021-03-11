var vm = new Vue({
    el: '#backups',
    delimiters: ["{[", "]}"],
    data: {
        backups: []
    },
    computed: {},
    methods: {
        getData() {
            axios.get('/backups/json/')
                .then(response => {
                    this.backups = response.data;
                });
        },
        deleteBackup(id) {
            axios.post(`/backups/delete/${id}/`, {})
                .then(response => {
                    this.backups = this.backups.filter(item => item.id !== id)
                })
        },
        createBackup() {
            axios.post('/backups/create/', {})
                .then(response => {
                    iziToast.success({
                        timeout: 3000,
                        position: 'topLeft',
                        message: 'Процесс начался. Обновите страницу через несколько минут.',
                    });
                })
        }
    },
    watch: {},
    created: function () {
    },
    mounted: function () {
        this.getData();
    }
});