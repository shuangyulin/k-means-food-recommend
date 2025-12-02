import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import xueshengList from '../pages/xuesheng/list'
import xueshengDetail from '../pages/xuesheng/detail'
import xueshengAdd from '../pages/xuesheng/add'
import meishiinfoList from '../pages/meishiinfo/list'
import meishiinfoDetail from '../pages/meishiinfo/detail'
import meishiinfoAdd from '../pages/meishiinfo/add'
import meishiinfoforecastList from '../pages/meishiinfoforecast/list'
import meishiinfoforecastDetail from '../pages/meishiinfoforecast/detail'
import meishiinfoforecastAdd from '../pages/meishiinfoforecast/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import discussmeishiinfoList from '../pages/discussmeishiinfo/list'
import discussmeishiinfoDetail from '../pages/discussmeishiinfo/detail'
import discussmeishiinfoAdd from '../pages/discussmeishiinfo/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'xuesheng',
					component: xueshengList
				},
				{
					path: 'xueshengDetail',
					component: xueshengDetail
				},
				{
					path: 'xueshengAdd',
					component: xueshengAdd
				},
				{
					path: 'meishiinfo',
					component: meishiinfoList
				},
				{
					path: 'meishiinfoDetail',
					component: meishiinfoDetail
				},
				{
					path: 'meishiinfoAdd',
					component: meishiinfoAdd
				},
				{
					path: 'meishiinfoforecast',
					component: meishiinfoforecastList
				},
				{
					path: 'meishiinfoforecastDetail',
					component: meishiinfoforecastDetail
				},
				{
					path: 'meishiinfoforecastAdd',
					component: meishiinfoforecastAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'discussmeishiinfo',
					component: discussmeishiinfoList
				},
				{
					path: 'discussmeishiinfoDetail',
					component: discussmeishiinfoDetail
				},
				{
					path: 'discussmeishiinfoAdd',
					component: discussmeishiinfoAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
