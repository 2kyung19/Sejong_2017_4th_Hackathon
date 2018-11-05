<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>

<%@ include file="../include/head.jsp"%>

<body class="hold-transition skin-red sidebar-mini">

<div class="wrapper">

    <!-- Main Header -->
    <%@ include file="../include/main_header.jsp"%>

    <!-- Left side column. contains the logo and sidebar -->
    <%@ include file="../include/left_column.jsp"%>

    <!-- Content Wrapper. Contains page content -->
    <div class="content-wrapper">
        <!-- Content Header (Page header) -->
        <section class="content-header">
            <h1>
                게시판
                <small>조회페이지</small>
            </h1>
            <ol class="breadcrumb">
                <li><i class="fa fa-edit"></i> article</li>
                <li class="active"><a href="${path}/article/write"> read</a></li>
            </ol>
        </section>

        <!-- Main content -->
        <section class="content">
            <!-- Info boxes -->
            <!-- Content Header (Page header) -->
            <section class="content-header">
                <h1>
                    Flot Charts
                    <small>preview sample</small>
                </h1>
                <ol class="breadcrumb">
                    <li><a href="#"><i class="fa fa-dashboard"></i> Home</a></li>
                    <li><a href="#">Charts</a></li>
                    <li class="active">Flot</li>
                </ol>
            </section>

            <!-- Main content -->
            <section class="content">
                <div class="row">
                </div>
                <div class="box-body">
                    <div id="donut-chart" style="height: 300px;"></div>
                </div>
                <!-- /.box-body-->
            </section>
            <!-- /.content -->

        </section>
    </div>

    <!-- Main Footer -->
    <%@ include file="../include/main_footer.jsp"%>

</div>
<!-- ./wrapper -->
<%@ include file="../include/plugin_js.jsp"%>

<script>
</script>

</body>
</html>