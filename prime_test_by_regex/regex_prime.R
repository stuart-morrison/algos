regex_prime <- function(n) {
	return(!grepl(pattern = "^1?$|^(11+?)\\1+?$", x = paste0(rep(1, n), collapse = "")))
}