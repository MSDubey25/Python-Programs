#File operations and description
#close() - closes a file if open else no effect
#detach() - seperate the underlying binary buffer from the TextIOBase and return it
#fileno() - return the file descriptor no
#flush() - flush the write buffer of the file stream
#isatty() - returns True if the file strea is interactive
#read(n) - read n characters from file if 0/-1 returns the whole file
#readable() - returns True if the file stream can be read
#readline(n=-1) - read and return one line from the file
#readlines(n=-1) - read and returns list of lines from the file
#seek(offset,from=seek_set) - change the file position to offset byte in reference to from(start,current,end)
#seekable() - returns true if the file stream supports random access
#tell() - returns the current file location
#truncate(size=None) - Resize the file stream to size byte if size not specified resize to current location
#writable() - returns true if the file stream can be written to
#write(s) - write String s to the file stream and returns the no of characters written
#writelines(lines) - write a list of lines to the files 
#readline(n=.1) - read and return one line from the file & reads at most n bytes if specified
#readlines(n=.1) - read and returns list of lines from the file & read atmost n bytes/characters if specified

print("contains the decription of file I/O operations")


