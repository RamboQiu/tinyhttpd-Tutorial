#!/usr/bin/perl -Tw

use strict; #为了帮助我们寻找错误拼写造成的错误
use CGI; #通过use关键字引入CGI模块

my($cgi) = new CGI;  #创建一个新的CGI对象

print $cgi->header; #输出CGI的标准头部信息
my($color) = "blue";  #创建变量color并默认为blue
$color = $cgi->param('color') if defined $cgi->param('color');

print $cgi->start_html(-title => uc($color),
                       -BGCOLOR => $color);
print $cgi->h1("This is $color");
print $cgi->end_html;
