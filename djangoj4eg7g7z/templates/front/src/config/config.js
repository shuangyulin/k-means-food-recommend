export default {
	baseUrl: 'http://localhost:8080/djangoj4eg7g7z/',
	name: '/djangoj4eg7g7z',
	indexNav: [
		{
			name: '美食信息',
			url: '/index/meishiinfo',
		},
		{
			name: '校园资讯',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '校园资讯',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
