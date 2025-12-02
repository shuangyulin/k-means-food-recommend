<template>
	<div>
		<div class="register-container">
			<div class="register-swiper3">
				<div class="swiper-container mySwiper3">
					<div class="swiper-wrapper">
						<div class="swiper-slide" v-for="(item,index) in swiperList" :key="item.id">
							<div>
								<el-image :src="item.url" fit="cover"></el-image>
							</div>
						</div>
					</div>
					<!-- Add Pagination -->
					<div class="swiper-pagination"></div>
					<!-- Add Arrows -->
					<div class="swiper-button-next">
						<span class="icon iconfont icon-jiantou18"></span>
					</div>
					<div class="swiper-button-prev">
						<span class="icon iconfont icon-jiantou39"></span>
					</div>
				</div>
			</div>
			<el-form v-if="pageFlag=='register'" ref="ruleForm" class="rgs-form animate__animated animate__flipInY" :model="ruleForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于k-means算法的校园美食推荐系统</div>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('xueshengzhanghao')?'required':''">学生账号：</div>
						<el-input  v-model="ruleForm.xueshengzhanghao"  autocomplete="off" placeholder="学生账号"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input  v-model="ruleForm.mima"  autocomplete="off" placeholder="密码"  type="password"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input  v-model="ruleForm.mima2" autocomplete="off" placeholder="确认密码" type="password" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('xueshengxingming')?'required':''">学生姓名：</div>
						<el-input  v-model="ruleForm.xueshengxingming"  autocomplete="off" placeholder="学生姓名"  type="text"  />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="ruleForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in xueshengxingbieOptions"
								v-bind:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="3"
							:multiple="true"
							:fileUrls="ruleForm.touxiang?ruleForm.touxiang:''"
							@change="xueshengtouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'">
						<div class="lable" :class="changeRules('lianxifangshi')?'required':''">联系方式：</div>
						<el-input  v-model="ruleForm.lianxifangshi"  autocomplete="off" placeholder="联系方式"  type="text"  />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">已有账号，直接登录</div>
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css'
	import Swiper from "swiper";
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
            xueshengxingbieOptions: [],
			swiperList: [{"name":"001.jpg","uid":1728874256297,"url":"http://codegen.caihongy.cn/20241014/71de9d5284bf4a4fbf9483cd76c40642.jpg","status":"success"},{"name":"002.jpg","uid":1728874260199,"url":"http://codegen.caihongy.cn/20241014/5ba89b3b5e1442328e6414aca4ec9303.jpg","status":"success"},{"name":"003.jpg","uid":1728874269236,"url":"http://codegen.caihongy.cn/20241014/018ac67a47334f6e8383a26518bfd27e.jpg","status":"success"}],
		};
	},
	mounted(){
		setTimeout(()=>{
			new Swiper(".mySwiper3", {"navigation":{"nextEl":".swiper-button-next","prevEl":".swiper-button-prev"},"pagination":{"el":".swiper-pagination","clickable":true},"autoplay":{"delay":2500,"disableOnInteraction":false},"effect":"fade"})
		}, 500)
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
			if(this.tableName=='xuesheng'){
				this.ruleForm = {
					xueshengzhanghao: '',
					mima: '',
					xueshengxingming: '',
					xingbie: '',
					touxiang: '',
					lianxifangshi: '',
				}
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xueshengzhanghao = [{ required: true, message: '请输入学生账号', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xueshengxingming = [{ required: true, message: '请输入学生姓名', trigger: 'blur' }]
			}
			this.xueshengxingbieOptions = "男,女".split(',')
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},
        xueshengtouxiangUploadChange(fileUrls) {
            this.ruleForm.touxiang = fileUrls;
        },

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			if((!this.ruleForm.xueshengzhanghao) && `xuesheng` == this.tableName){
				this.$message.error(`学生账号不能为空`);
				return
			}
			if((!this.ruleForm.mima) && `xuesheng` == this.tableName){
				this.$message.error(`密码不能为空`);
				return
			}
			if((this.ruleForm.mima!=this.ruleForm.mima2) && `xuesheng` == this.tableName){
				this.$message.error(`两次密码输入不一致`);
				return
			}
			if((!this.ruleForm.xueshengxingming) && `xuesheng` == this.tableName){
				this.$message.error(`学生姓名不能为空`);
				return
			}
            if(this.ruleForm.touxiang!=null) {
                this.ruleForm.touxiang = this.ruleForm.touxiang.replace(new RegExp(this.$base.url,"g"),"");
            }
			if(`xuesheng` == this.tableName && this.ruleForm.lianxifangshi &&(!this.$validate.isMobile(this.ruleForm.lianxifangshi))){
				this.$message.error(`联系方式应输入手机格式`);
				return
			}
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
	background-repeat: no-repeat;
	background-size: cover;
	background: url(http://codegen.caihongy.cn/20241013/62c0a2dc820a4e83a2bcdf4b8996becd.jpg);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center bottom;
	.register-swiper3 {
		margin: 0 auto;
		z-index: auto;
		top: 0;
		left: 0;
		width: 100vw;
		position: fixed;
		height: 100vh;
		.swiper-container {
			.swiper-slide {
				div {
					width: 100%;
					height: 100vh;
					.el-image {
						object-fit: cover;
						width: 100%;
						height: 100vh;
					}
				}
			}
			.swiper-pagination{
				left: 0;
				bottom: 10px;
				width: 100%;
				/deep/ span.swiper-pagination-bullet {
					border-radius: 100%;
					margin: 0 4px;
					background: #000;
					display: inline-block;
					width: 8px;
					opacity: .2;
					height: 8px;
				}
				/deep/ span.swiper-pagination-bullet:hover {
					background: #fff;
					opacity: 1;
				}
				/deep/ span.swiper-pagination-bullet.swiper-pagination-bullet-active {
					background: #fff;
					opacity: 1;
				}
			}
			.swiper-button-next {
				margin: -12px 0 0;
				top: 50%;
				display: none;
				width: 24px;
				height: 24px;
				.iconfont {
					color: #fff;
					width: 24px;
					font-size: 24px;
					height: 24px;
				}
			}
			.swiper-button-prev {
				margin: -12px 0 0;
				top: 50%;
				display: none;
				width: 24px;
				height: 24px;
				.iconfont {
					color: #fff;
					width: 24px;
					font-size: 24px;
					height: 24px;
				}
			}
			
			.swiper-button-prev:after {
				display:none;
			}
			.swiper-button-next:after {
				display:none;
			}
		}
	}
	.rgs-form {
		.rgs-form2 {
		border-radius: 12px;
		padding: 40px 40px 10px 40px;
		background: #fff;
		width: 100%;
		}
		border-radius: 12px;
		padding: 80px 20px 90px;
		margin: 20px 0;
		z-index: 1000;
		flex-direction: column;
		background: rgba(0, 0, 0, .5);
		display: flex;
		width: 600px;
		align-items: center;
		position: relative;
		flex-wrap: wrap;
		height: auto;
		.title {
			padding: 0 0px;
			margin: 0 0 20px 0px;
			color: #fff;
			white-space: nowrap;
			font-weight: 600;
			font-size: 18px;
			line-height: 40px;
			top: 20px;
			left: 0;
			background: noner;
			width: 100%;
			position: absolute;
			text-align: center;
		}
		.list-item {
			padding: 0 0 0 0px;
			margin: 0 0 20px;
			width: 100%;
			position: relative;
			height: auto;
			/deep/ .el-form-item__content {
				display: block;
			}
			.lable {
				color: #333;
				display: inline-block;
				width: 100%;
				font-size: 16px;
				line-height: 40px;
				text-align: left;
			}
			.el-input {
				width: 100%;
			}
			.el-input /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			.el-input /deep/ .el-input__inner:focus {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				outline: none;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			.el-input-number {
				width: 100%;
			}
			.el-input-number /deep/ .el-input__inner {
				text-align: center;
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			.el-input-number /deep/ .el-input__inner:focus {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				outline: none;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			.el-input-number /deep/ .el-input-number__decrease {
				display: none;
			}
			.el-input-number /deep/ .el-input-number__increase {
				display: none;
			}
			.el-select {
				width: 100%;
			}
			.el-select /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.el-select /deep/ .el-input__inner:focus {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px;
				outline: none;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor /deep/ .el-input__inner {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px 0 30px;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.el-date-editor /deep/ .el-input__inner:focus {
				border: 0px solid #efeff7;
				border-radius: 6px;
				padding: 0 10px 0 30px;
				outline: none;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 16px;
				height: 40px;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			/deep/ .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			/deep/ .upload .upload-img {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 6px;
				color: #999;
				background: #f5f5f5;
				width: 120px;
				font-size: 24px;
				line-height: 48px;
				text-align: center;
				height: 48px;
			}
			/deep/ .el-upload-list .el-upload-list__item {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 6px;
				color: #999;
				background: #f5f5f5;
				width: 120px;
				font-size: 24px;
				line-height: 48px;
				text-align: center;
				height: 48px;
			}
			/deep/ .el-upload .el-icon-plus {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 6px;
				color: #999;
				background: #f5f5f5;
				width: 120px;
				font-size: 24px;
				line-height: 48px;
				text-align: center;
				height: 48px;
			}
			/deep/ .el-upload__tip {
				color: #666;
				font-size: 15px;
			}
			/deep/ .el-input__inner::placeholder {
				color: #999;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				position: inherit !important;
				content: "*";
				order: -1;
			}
			.editor {
				border: 1px solid #eee;
				background: #fff;
				width: 100%;
				min-height: 250px;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 0px solid #efeff7;
				border-radius: 6px 0 0 6px;
				padding: 0 10px;
				margin: 0;
				color: #999;
				background: #f5f5f5;
				flex: 1;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			input:focus {
				border: 0px solid #efeff7;
				border-radius: 6px 0 0 6px;
				padding: 0 10px;
				outline: none;
				color: #999;
				background: #f5f5f5;
				width: 100%;
				font-size: 14px;
				height: 40px;
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			button {
				border: 0px solid #efeff7;
				cursor: pointer;
				border-radius: 0 6px 6px 0;
				padding: 0;
				margin: 0px 0 0 0px;
				color: #fff;
				background: #05aeff;
				width: 150px;
				font-size: 15px;
				height: 40px;
			}
			button:hover {
				opacity: 1;
			}
		}
		.register-btn {
			margin: 0;
			width: calc(100% + 0px);
		}
		.register-btn1 {
			margin: 0;
			left: 20px;
			bottom: 10px;
			width: calc(100% - 40px);
			position: absolute;
			order: 2;
		}
		.register-btn2 {
			width: 100%;
		}
		.r-btn {
			border: 0px solid rgba(0, 0, 0, 1);
			cursor: pointer;
			padding: 0 10px;
			margin: 0 0 10px;
			color: #fff;
			font-weight: 600;
			letter-spacing: 2px;
			font-size: 24px;
			border-radius: 12px;
			background: #05aeff;
			width: 100%;
			min-width: 68px;
			height: 60px;
		}
		.r-btn:hover {
			opacity: 1;
		}
		.r-login {
			cursor: pointer;
			padding: 0;
			color: #999;
			display: inline-block;
			width: 100%;
			font-size: 15px;
			line-height: 40px;
			text-align: center;
		}
		.r-login:hover {
		}
	}
}
	
	::-webkit-scrollbar {
	  display: none;
	}
</style>
