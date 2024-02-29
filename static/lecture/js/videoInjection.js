function videoInjection(url) {
    app = new Vue({
        delimiters: ["[[", "]]"],
        el: '#courseBody',
        data: {
            picked_video_id: null,
            picked_video_url: $("#video-list .video-list--input").eq(0).attr("value"),
            picked_video_second: 0,
            player: null
        },
        mounted() {
            this.picked_video_id = this.$el.querySelector('.video').dataset.id;
            this.picked_video_url = this.$el.querySelector('.video').dataset.url;
            this.picked_video_second = this.$el.querySelector('.video').dataset.second;

            this.initPlyr();
            this.player.on('ready', event => {
                this.player.currentTime = parseFloat(this.picked_video_second);
            });
        },
        watch: {
            picked_video_url() {
                this.initPlyr();
            }
        },
        methods: {
            initPlyr() {
                if (this.player) {
                    this.player.destroy();
                }
                // 비디오 소스 직접 업데이트
                var videoElement = document.getElementById('player');
                var sourceElement = document.getElementById('videoSource');
                sourceElement.setAttribute('src', this.picked_video_url);
                videoElement.load();

                this.player = new Plyr(videoElement);
            }
        },
    });
    window.addEventListener('beforeunload', function(event) {
        var csrfToken = $('[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'post',
            async: false,
            headers: { 'X-CSRFToken': csrfToken },
            url,
            data: {
                seconds: app.player.currentTime,
                video_id: app.picked_video_id,
            },
        });
    });
}