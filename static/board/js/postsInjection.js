function postsInjection(post_list) {
    new Vue({
        delimiters: ["[[", "]]"],
        el: "#board",
        data: {
            searchQuery: '',
        },
        computed: {
            posts() {
                return post_list.filter(post => {
                    return post.title.toLowerCase().includes(this.searchQuery)
                        || post.author.toLowerCase().includes(this.searchQuery);
                });
            }
        }
    });
}