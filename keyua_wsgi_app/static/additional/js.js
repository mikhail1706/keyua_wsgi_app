if (response.data.success) {

    $data$

    iziToast.success({
        timeout: 3000,
        position: 'topLeft',
        message: response.data.msg,
    });
} else {
    iziToast.error({
        timeout: 3000,
        title: 'Error',
        message: response.data.msg,
    });
}


iziToast.success({
    timeout: 3000,
    position: 'topLeft',
    message: response.data.msg,
});

iziToast.error({
    timeout: 3000,
    title: 'Error',
    message: response.data.msg,
});


var vm = new Vue({
    el: '#app',
    delimiters: ["{[", "]}"],
    data: {},
    computed: {},
    methods: {},
    watch: {},
    created: function () {},
    mounted: function () {}
});

axios.post('url', {})
    .then(response => {
        if (!response.data.error) {

        }
    }).catch(error => {
        alert(error);
    })
    .then(e => {
    });

axios.all([
        axios.get('/api/questions'),
        axios.get('/api/recommendations'),
    ])
    .then(axios.spread((questions, recommendations) => {
            this.questions = questions.data;
            this.recommendations = recommendations.data;
        }
    ))
    .catch(error => {
        console.log(error);
    });