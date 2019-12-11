<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" import="java.util.*"%>
 
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
 
<table align='center' border='1' cellspacing='0'>
    <tr>
        <td>id</td>
        <td>name</td>
        <td>price</td>
        <td>删除</td>
		<td>编辑</td>
    </tr>
    <c:forEach items="${products}" var="c" varStatus="st">
        <tr>
            <td>${c.id}</td>
            <td>${c.name}</td>
            <td>${c.price}</td>
            <td><a href="editProduct?id=${c.id}">编辑</a></td>
            <td><a href="deleteProduct?id=${c.id}">删除</a></td>
        </tr>
    </c:forEach>
    <div style="text-align:center">
        <a href="?start=0">首  页</a>
        <a href="?start=${page.getup()}">上一页</a>
        <a href="?start=${page.getdown()}">下一页</a>
        <a href="?start=${page.last}">末  页</a>
    </div>
    
    <div style="text-align:center;margin-top:40px">
		
		<form method="post" action="addProduct">
			商品名称： <input name="name" value="" type="text"> <br><br>
			商品价格： <input name="price" value="" type="text"> <br><br>
			<input type="submit" value="增加商品">
		</form>

	</div>	
</table>
