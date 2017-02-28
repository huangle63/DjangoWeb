$(function(){
	var PasswordRules = {
		letterPattern: /[a-zA-Z]+/,	//判断是否含有字母
		numbericPattern: /[0-9]+/,	//判断是否含有数字
		specialPattern: /[~!@#$%^&*()_+`\-=\[\]\\{}\|;':",\.\/<>\?]/,	//判断是否含有特殊符号
		illegalPattern: /[^a-zA-Z0-9~!@#$%^&*()_+`\-=\[\]\\{}\|;':",\.\/<>\?]+/,	//判断是否含有非法字符
		validate: function(pwd) {
			var len = pwd.length;
			var result = {
				success: false,
				strength: 'w',
				message: ''
			};

			if (len < 8) {
				result.message = '密码不能少于8位';
				return result;
			}
			if (len > 20) {
				result.message = '密码不能多于20位';
				return message;
			}

			var category = this.calcCharsCategory(pwd);
			if (category <= 1) {
				result.message = "请输入8-20位字母、数字和符号两种及以上组合";
				return result;
			}

			if (category === 2) {
				if (len >= 8 && len <= 11) {
					result.success = true;
					result.strength = 'm';
				} else if (len > 11 && len <= 20) {
					result.success = true;
					result.strength = 's';
				} else {
					result.success = false;
					result.strength = 's';
				}
			} else {
				if (len >= 8 && len <= 9) {
					result.success = true;
					result.strength = 'm';
				} else if (len > 9 && len <= 20) {
					result.success = true;
					result.strength = 's';
				} else {
					result.success = false;
					result.strength = 's';
				}
			}

			if (this.illegalPattern.test(pwd)) {
				result.success = false;
				result.message = "密码中包含非法字符";
				result.strength = 'w';
			}
			
			if(pwd==$("#J_input_user").val())
			{
				result.success = false;
				result.message = "密码不能和邮箱、手机和用户名相同";
			}

			return result;
		},
		calcCharsCategory: function(pwd) {	//计算字符串满足几种规则
			var category = 0;

			if (this.letterPattern.test(pwd)) {
				category++;
			}

			if (this.numbericPattern.test(pwd)) {
				category++;
			}

			if (this.specialPattern.test(pwd)) {
				category++;
			}

			return category;
		}
	};
	
	var UserRules = {
		validate: function(content, type) {
			var n = $.trim(content),
				//type = loginValidate.regMethod,
				result = {
				    success: false,
					message: ''
				};
			if(type == 'user'){
				if (/^[a-zA-Z0-9]{3,30}$/i.test(n)) {
					var url = "/validate/validate_username";
					$.ajax({
						type : "post",
						data : {username:n},
						dataType : "json",
						url : url,
						async: false,
						success : function(res) {
//							data=$.parseJSON(result);
							if(res.resultCode==0)
							{
								result.success = true;
							}
							else
							{
								result.success = false;
								result.message =res.message;
							}
						},
						error : function(data) {
						}
					})

				} else {
					result.success = false;
					result.message ='用户名由3-30位数字字母组成'
				}
			}else if(type == 'email'){
				if(/^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(n)){
					var url = "/validate/validate_email";
					$.ajax({
						type : "post",
						data : {email:n},
						dataType : "json",
						url : url,
						async: false,
						success : function(res) {
							if(res.resultCode==0)
							{
								result.success = true;
							}
							else
							{
								result.success = false;
								result.message =res.message;
							}
						},
						error : function(data) {
						}
					})
				}else{
					result.success = false;
					result.message ='请输入正确的邮箱格式';
				}
			}
//			else if(type == 'phone'){
//				if(/^[1][3,4,5,7,8][0-9]{9}$/.test(n)){
//					var url = contextPath + "/sso/validate_mobile.json";
//					$.ajax({
//						type : "post",
//						data : {mobilePhone:n},
//						dataType : "json",
//						url : url,
//						async: false,
//						success : function(r) {
//							if (r.success) {
//
//								data=$.parseJSON(r.data);
//								if(data.resultCode==0)
//								{
//									result.success = true;
//								}
//								else
//								{
//									result.success = false;
//									result.message =data.errorDesc;
//								}
//
//							} else {
//								alert(r.message);
//							}
//						},
//						error : function(data) {
//						}
//					})
//				}else{
//					result.success = false;
//					result.message ='请输入正确的手机号码';
//				}
//			}
			return result;
		}
	}

	var signupValidate = {
		eleGroup: {
			regForm: $('#regForm'),
			regButton: $('#regbtn'),
			userInput: $('#user'),
			userErr: $('#form_user_err'),
			emailInput: $('#email'),
			emailErr: $('#form_email_err'),
			pwInput: $('#password'),
			pwErr: $('#form_password_err'),
			pw1Input: $('#password_confirm'),
			pw1Err: $('#form_password_confirm_err'),
            submitErr: $('#form_submit_err')
		},
		init: function() {
		    this.initEvent();
		    this.signup();
		},
		initEvent:function(){
			signupValidate.eleGroup.userErr.hide();
			signupValidate.eleGroup.emailErr.hide();
			signupValidate.eleGroup.pwErr.hide();
			signupValidate.eleGroup.pw1Err.hide();

		},
		signup: function() {
			var usernameRe = UserRules.validate(signupValidate.eleGroup.userInput.val(), 'user');
			if(usernameRe.success == false){
				signupValidate.eleGroup.userErr.text(usernameRe.message);
				signupValidate.eleGroup.userErr[0].style.display = "inline";
				//signupValidate.eleGroup.userErr.show();
				return false;
			}

			var emailRe = UserRules.validate(signupValidate.eleGroup.emailInput.val(), 'email');
			if(emailRe.success == false){
				signupValidate.eleGroup.emailErr.text(emailRe.message);
				signupValidate.eleGroup.emailErr[0].style.display = "inline";
				return false;
			}
			var passwordRe = PasswordRules.validate(signupValidate.eleGroup.pwInput.val());
			if(passwordRe.success == false){
				signupValidate.eleGroup.pwErr.text(passwordRe.message);
				signupValidate.eleGroup.pwErr[0].style.display = "inline";
				return false;
			}
			var p1 = signupValidate.eleGroup.pwInput.val(),
				p2 = signupValidate.eleGroup.pw1Input.val();
			if(p1 != p2){
				signupValidate.eleGroup.pw1Err.text('两次密码不一致');
				signupValidate.eleGroup.pw1Err[0].style.display = "inline";
				return false;
			}
			$.ajax({
				type:"POST",
				url:"/signup/",
//				data: signupValidate.eleGroup.regForm.serialize(),
				data: {form_user: signupValidate.eleGroup.userInput.val(),
				        form_email: signupValidate.eleGroup.emailInput.val(),
				        form_password: signupValidate.eleGroup.pwInput.val()
				},
				async:false,
				success: function(res) {
                    signupValidate.eleGroup.submitErr.text('注册成功，等待跳转');
				    signupValidate.eleGroup.submitErr[0].style.display = "inline";
					location.href = "/"
				},
				error: function(data) {

				}
			});
		}
	};
	$('#regbtn').click(function() {
		signupValidate.init();
	});
	
	$('#button_A').click(function(){
		var result = PasswordRules.validate($('#password').val());
		alert(result.message);
	});

});
