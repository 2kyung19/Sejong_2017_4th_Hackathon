<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<aside class="main-sidebar">

    <!-- sidebar: style can be found in sidebar.less -->
    <section class="sidebar">

        <!-- Sidebar user panel (optional) -->
        <div class="user-panel">
            <div class="pull-left image">
                <img src="/dist/img/user2-160x160.jpg" class="img-circle" alt="User Image">
            </div>
            <div class="pull-left info">
                <p>Alexander Pierce</p>
                <!-- Status -->
                <a href="#"><i class="fa fa-circle text-success"></i> Online</a>
            </div>
        </div>

        <!-- search form (Optional) -->
        <form action="#" method="get" class="sidebar-form">
            <div class="input-group">
                <input type="text" name="q" class="form-control" placeholder="Search...">
                <span class="input-group-btn">
              <button type="submit" name="search" id="search-btn" class="btn btn-flat"><i class="fa fa-search"></i>
              </button>
            </span>
            </div>
        </form>
        <!-- /.search form -->

        <!-- Sidebar Menu -->
        <ul class="sidebar-menu" data-widget="tree">

            <li class="header">트랙 관리</li>
            <li><a href="${path}/article/list"><i class="fa fa-sitemap"></i> <span>SW 대학 트랙 현황</span></a></li>
            <li><a href="${path}/article/list"><i class="fa fa-map-o"></i> <span>자신의 전체 트랙 현황</span></a></li>
            <li><a href="${path}/article/list"><i class="fa fa-map-signs"></i> <span>자신의 신청 트랙 현황</span></a></li>
            <li class="header">공지사항</li>
            <li><a href="${path}/article/write"><i class="fa fa-newspaper-o"></i> <span>공지사항</span></a></li>
            <li><a href="${path}/article/write"><i class="fa fa-comments-o"></i> <span>자주 묻는 질문</span></a></li>
            <li class="header">시스템</li>
            <li><a href="${path}/article/write"><i class="fa fa-exclamation-circle"></i> <span>시스템 오류 신고</span></a> </li>
            <li><a href="${path}/article/write"><i class="fa fa-gears"></i> <span>시스템 정보</span></a></li>
        </ul>
        <!-- /.sidebar-menu -->
    </section>
    <!-- /.sidebar -->
</aside>