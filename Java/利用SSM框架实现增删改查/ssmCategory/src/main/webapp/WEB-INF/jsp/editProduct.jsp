<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.*"%>
 
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
 
 <div style="width:500px;margin:0px auto;text-align:center">
	
	
	<div style="text-align:center;margin-top:40px">
		
		<form method="post" action="updateProduct">
			产品名称： <input name="name" value="${product.name}" type="text"> <br><br>
			产品价格： <input name="price" value="${product.price}" type="text"> <br><br>
			<input type="hidden" value="${product.id}" name="id">
			<input type="submit" value="修改产品">
		</form>

	</div>	
 </div>
