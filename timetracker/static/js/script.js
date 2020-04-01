Vue.component('AppDuration', {
    props: ['duration'],
    computed: {
        duration_humanize: function () {
            let d = moment.duration(1000 * this.duration);
            let minutes = '' + d.minutes();
            let hours = '' + d.hours();
            let days = '' + d.days();
            let months = '' + d.months();
            let years = '' + d.years();
            minutes = minutes.length < 2 ? '0' + minutes : minutes;
            hours = hours.length < 2 ? '0' + hours : hours;
            console.log(minutes, hours);
            let duration = minutes + 'min';
            duration = hours + 'h ' + duration;
            if (days > 0) duration = days + ' days ' + duration;
            if (months > 0) duration = months + ' months ' + duration;
            if (years > 0) duration = years + ' years ' + duration;
            return duration;
        }
    },
    template: '<span>{{ duration_humanize }}</span>'
});

var app = new Vue({
    el: '#app',
});

