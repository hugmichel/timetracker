Vue.component('AppDuration', {
    props: ['duration'],
    computed: {
        duration_humanize: function () {
            let d = moment.duration(1000 * this.duration);
            let duration = d.seconds() + ' seconds';
            if (d.minutes() > 0) duration = d.minutes() + ' minutes ' + duration;
            if (d.hours() > 0) duration = d.hours() + ' hours ' + duration;
            if (d.days() > 0) duration = d.days() + ' days ' + duration;
            if (d.months() > 0) duration = d.months() + ' months ' + duration;
            if (d.years() > 0) duration = d.years() + ' years ' + duration;
            return duration;
        }
    },
    template: '<span>{{ duration_humanize }}</span>'
});
var app = new Vue({
    el: '#app',
})

