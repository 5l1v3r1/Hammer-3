##
# This file is part of WhatWeb and may be subject to
# redistribution and commercial restrictions. Please see the WhatWeb
# web site for more information on licensing and terms of use.
# http://www.morningstarsecurity.com/research/whatweb
##
Plugin.define "LXR" do
author "Brendan Coles <bcoles@gmail.com>" # 2011-05-19
version "0.1"
description 'LXR (formerly "the Linux Cross Referencer") is a general purpose source code indexer and cross-referencer that provides web-based browsing of source code with links to the definition and usage of any identifier. Supports multiple languages. - Homepage: http://lxr.linux.no/'

# Google results as at 2011-05-19 #
# 82 for "This page was automatically generated by the LXR engine."
# 72 for "Visit the LXR main site for more information."

# Dorks #
dorks [
'"This page was automatically generated by the LXR engine."'
]



# Matches #
matches [

# automatically generated by link
{ :regexp=>/<hr>\nThis page was automatically generated by the \n<a href="http:blurb\.html">LXR engine<\/a>\.\n<br>\nVisit the <a href="http:\/\/lxr\.linux\.no\/">LXR main site<\/a> for more\ninformation\./ },

# Identifier search link
{ :text=>'<b>[</b>&nbsp;<a href="ident">identifier search</a>&nbsp;<b>]</b>' },
{ :text=>'[&nbsp;<a href="ident">identifier search</a>&nbsp;]' },

]

end


