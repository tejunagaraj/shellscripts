#!/usr/bin/ruby -w


print <<EOF
	This is the first way of creating
	here document ie. multiple line string.
EOF

print <<"EOF";
	This is the second way of creating
	here document ie. multiple line string.
EOF

print <<`EOF`
	echo hi there
	echo lo there
EOF

print <<"foo", <<"bar"
	I said foo.
foo
	I said bar.
bar
