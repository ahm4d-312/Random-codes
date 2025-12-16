	.file	"hello_world.cpp"
	.intel_syntax noprefix
	.text
	.section	.rodata
.LC0:
	.string	"Hello World!"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	lea	rax, .LC0[rip]
	mov	rdi, rax
	mov	eax, 0
	call	printf@PLT
	mov	eax, 0
	pop	rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (GNU) 15.2.1 20251112"
	.section	.note.GNU-stack,"",@progbits
