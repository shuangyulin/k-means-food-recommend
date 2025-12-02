const base = {
    get() {
        return {
            url : "http://localhost:8080/djangoj4eg7g7z/",
            name: "djangoj4eg7g7z",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "基于k-means算法的校园美食推荐系统"
        } 
    }
}
export default base
