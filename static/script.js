html = document.getElementById("html");
python = document.getElementById("python");
css = document.getElementById("css");
js = document.getElementById("js");
tailwind = document.getElementById("tailwind");
bootstrap = document.getElementById("bootstrap");
main_con = document.getElementById("main-con");
card_container_html = document.getElementById("card-container-html");
card_container_python = document.getElementById("card-container-python");
card_container_css = document.getElementById("card-container-css");
card_container_js = document.getElementById("card-container-js");
card_container_c = document.getElementById("card-container-c");
card_container_tailwind = document.getElementById("card-container-tailwind");
card_container_bootstrap = document.getElementById("card-container-bootstrap");

function toggleHiddenHtml() {
	if (card_container_html.hasAttribute("hidden")) {
		card_container_html.removeAttribute("hidden");
	} else {
		card_container_html.setAttribute("hidden", "");
	}
}

function toggleHiddenPython() {
	if (card_container_python.hasAttribute("hidden")) {
		card_container_python.removeAttribute("hidden");
	} else {
		card_container_python.setAttribute("hidden", "");
	}
}

function toggleHiddenCSS() {
	if (card_container_css.hasAttribute("hidden")) {
		card_container_css.removeAttribute("hidden");
	} else {
		card_container_css.setAttribute("hidden", "");
	}
}

function toggleHiddenJS() {
	if (card_container_js.hasAttribute("hidden")) {
		card_container_js.removeAttribute("hidden");
	} else {
		card_container_js.setAttribute("hidden", "");
	}
}

function toggleHiddenTailwind() {
	if (card_container_tailwind.hasAttribute("hidden")) {
		card_container_tailwind.removeAttribute("hidden");
	} else {
		card_container_tailwind.setAttribute("hidden", "");
	}
}

function toggleHiddenBootstrap() {
	if (card_container_bootstrap.hasAttribute("hidden")) {
		card_container_bootstrap.removeAttribute("hidden");
	} else {
		card_container_bootstrap.setAttribute("hidden", "");
	}
}
html.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenHtml();
});
python.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenPython();
});
css.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenCSS();
});
js.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenJS();
});
tailwind.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenTailwind();
});
bootstrap.addEventListener("click", () => {
	if (main_con.classList.contains("highlight")) {
		main_con.classList.remove("highlight");
	} else {
		main_con.classList.add("highlight");
	}
	// main_con.classList.add("highlight");
	toggleHiddenBootstrap();
});
