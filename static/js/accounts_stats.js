// *********** Values **********
let spent = 0;
let income = 0;

class Budget {
	constructor(account_type, description, amount) {
		this.account_type = account_type;
		this.description = description;
		this.amount = amount;
	}
	static addBudget(entry) {
		let budget;
		if (localStorage.getItem("budget") === null) {
			budget = [];
		} else {
			budget = JSON.parse(localStorage.getItem("budget"));
		}
		budget.push(entry);
		localStorage.setItem("budget", JSON.stringify(budget));
	}
}

class UI {
	static displayAddedBudget(budget) {
		if (budget.account_type === "debit") {
			const expsenseOutPut = document.querySelector(".expenses-result");
			const li = document.createElement("li");
			li.className = "table";
			const span1 = document.createElement("span");
			span1.className = "expense-text";
			span1.innerText = budget.description;
			li.appendChild(span1);
			const div = document.createElement("div");
			div.className = "expenses-div";
			const span2 = document.createElement("span");
			span2.className = "expenses-values";
			span2.innerText = "- " + parseFloat(budget.amount).toFixed(2);
			div.appendChild(span2);
			if (income > 0) {
				const span3 = document.createElement("span");
				span3.className = "expense-percent";
				span3.innerText = `${Math.ceil((budget.amount / income) * 100)}%`;
				div.appendChild(span3);
			}
			const span4 = document.createElement("i");
			span4.className = "fas fa-times red ";
			div.appendChild(span4);
			li.appendChild(div);
			expsenseOutPut.appendChild(li);

			// expenses += parseFloat(budget.amount).toFixed(2);
		} else if (budget.account_type === "credit") {
			const expsenseOutPut = document.querySelector(".income-result");
			const li = document.createElement("li");
			li.className = "table";
			const span1 = document.createElement("span");
			span1.className = "income-text";
			span1.innerText = budget.description;
			li.appendChild(span1);
			const div = document.createElement("div");
			div.className = "income-values";
			const span2 = document.createElement("span");
			span2.className = "income-values";
			span2.innerText = "+ " + parseFloat(budget.amount).toFixed(2);
			div.appendChild(span2);
			const span3 = document.createElement("i");
			span3.className = "fas fa-times green ";
			div.appendChild(span3);
			li.appendChild(div);
			expsenseOutPut.appendChild(li);
			// income += parseFloat(budget.amount).toFixed(2);
		}
	}

	static displayFromLS() {
		const budget = JSON.parse(localStorage.getItem("budget"));

		// ****** remove all table element before they are reset ****
		let tableList = document.getElementsByClassName("table");
		tableList = Array.from(tableList);
		tableList.forEach((element) => {
			element.remove();
		});

		if (budget !== null) {
			spent = 0;
			income = 0;
			// ********* get both total expenses and income ****
			budget.forEach((entry) => {
				if (entry.account_type === "debit") {
					spent += entry.amount;
				} else {
					income += entry.amount;
				}
			});

			// **** display income and expenses and % ***
			document.querySelector(".expense-total").innerText = "- " + spent.toFixed(2);
			if (income > 0) {
				document.querySelector(".expense-percent").innerText =
					Math.ceil((spent / income) * 100) + "%";
			}
			document.querySelector(".income-total").innerText = "+ " + income.toFixed(2);

			let diff;
			income - spent >= 0 ? (diff = "+ ") : (diff = "- ");

			document.querySelector("#currentpositive").innerText =
				diff + Math.abs(income - spent).toFixed(2);

			// ******* display each log in the budget ****
			budget.forEach((e) => {
				UI.displayAddedBudget(e);
			});
		}
	}
}

document.getElementById("submit").addEventListener("click", (e) => {
	const accountType = document.getElementById("account-type").value;
	const inputDesciption = document.getElementById("description-input").value;
	const amount = parseFloat(document.getElementById("amount").value);

	if (amount.length === 0 || inputDesciption.length === 0) {
		console.log("something is wrong.");
	} else {
		const budget = new Budget(accountType, inputDesciption, amount);

		Budget.addBudget(budget);
		// const ui = new UI();

		UI.displayFromLS();
	}
	document.getElementById("description-input").value = "";
	document.getElementById("amount").value = "";
	// e.preventDefault();
});

window.addEventListener("DOMContentLoaded", () => {
	if ("loader") {
		UI.displayFromLS();
	}
});

const expensesUL = document.querySelector(".expenses-result");
const incomesUL = document.querySelector(".income-result");

const removerList = [expensesUL, incomesUL];
removerList.forEach((element) => {
	element.addEventListener("click", (e) => {
		if (e.target.classList.contains("fa-times")) {
			const remover =
				e.target.parentElement.parentElement.firstElementChild.innerText;
			const budget = JSON.parse(localStorage.getItem("budget"));

			budget.forEach((e, index) => {
				if (e.description === remover) {
					budget.splice(index, 1);
				}
			});
			localStorage.setItem("budget", JSON.stringify(budget));

			UI.displayFromLS();
		}
	});
});

const inputDescription = document.getElementById("description-input");
const selector = document.getElementById("account-type");
const inputAmount = document.getElementById("amount");
const submitButton = document.querySelector(".fa-check");
const submiting = document.getElementById("submit");

const focus = [inputDescription, inputAmount];

focus.forEach((e) => {
	e.addEventListener("focus", () => {
		if (selector.value === "debit") {
			inputDescription.classList.toggle("border-color-red");
			inputAmount.classList.toggle("border-color-red");
			selector.classList.toggle("border-color-red");
			submiting.classList.toggle("border-color-red");
			submitButton.classList.toggle("color-red");
		} else {
			inputDescription.classList.toggle("border-color-green");
			inputAmount.classList.toggle("border-color-green");
			selector.classList.toggle("border-color-green");
			submiting.classList.toggle("border-color-green");
			submitButton.classList.toggle("color-green");
		}
	});
});
focus.forEach((e) => {
	e.addEventListener("blur", () => {
		inputDescription.classList.remove("border-color-red");
		inputAmount.classList.remove("border-color-red");
		selector.classList.remove("border-color-red");
		submiting.classList.remove("border-color-red");
		submitButton.classList.remove("color-red");
		inputDescription.classList.remove("border-color-green");
		inputAmount.classList.remove("border-color-green");
		selector.classList.remove("border-color-green");
		submiting.classList.remove("border-color-green");
		submitButton.classList.remove("color-green");
	});
});

var testFunc = (function () {
	var x = 34;
	function add(a) {
		return x + a;
	}

	return {
		publicTest: function (b) {
			return add(b);
		},
	};
})();

class Elements {
	constructor(name, buildYear) {
		this.name = name;
		this.buildYear = buildYear;
	}
	static Adder(mapName, list) {
		mapName.set(list.name, list);
	}
}

class Park extends Elements {
	constructor(name, buildYear, parkSize, trees) {
		super(name, buildYear);
		this.parkSize = parkSize;
		this.trees = trees;
	}
}
class Street extends Elements {
	constructor(name, buildYear, len, streetSize = "normal") {
		super(name, buildYear);
		this.len = len;
		this.streetSize = streetSize;
	}
}

const parkMap = new Map();
const streetkMap = new Map();

const Green_Park = new Park("Green Park", 1990, 12);
// console.log(Green_Park);
// const National_Park = new Park("Green Park", 1970, 15);
// const Oak_Park = new Park("Green Park", 1980, 8);
// parkMap.set("Green Park", Green_Park);
// parkMap.set("National Park", National_Park);
// parkMap.set("Oak Park", Oak_Park);

Elements.Adder(parkMap, new Park("Green Park", 1990, 12, 700));
Elements.Adder(parkMap, new Park("Oak Park", 1980, 8, 950));
Elements.Adder(parkMap, new Park("National street", 1957, 15, 4000));
Elements.Adder(streetkMap, new Street("Evergreen street", 1990, 3, "tinny"));
Elements.Adder(streetkMap, new Street("Nelson steet", 1980, 2.4));
Elements.Adder(streetkMap, new Street("Harmon street", 1957, 1.3, "small"));
Elements.Adder(streetkMap, new Street("Washington street", 1987, 3.8, "huge"));

function parkOutput() {
	console.log("----- PARKS REPORT-----");
	let average = 0;
	parkMap.forEach((key) => {
		average += key.parkSize;
	});
	console.log(
		`Our ${parkMap.size} parks have an average age of ${
			average / parkMap.size
		} years`
	);
	parkMap.forEach((key) => {
		console.log(
			` ${key.name} has a tree density of ${
				key.trees / key.parkSize
			} per square km`
		);
	});
	parkMap.forEach((key) => {
		if (key[3] > 1000) {
			console.log(` ${key[0]} has more than a 1000 trees`);
		}
	});
}

parkOutput();

function streetOutput() {
	console.log("----- Street REPORT-----");
	let average = 0;
	// let total = 0
	streetkMap.forEach((key) => {
		average += key.len;
	});
	console.log(
		`Our ${
			streetkMap.size
		} streets have a total len of ${average} km with an average of ${
			average / streetkMap.size
		}`
	);
	streetkMap.forEach((key) => {
		console.log(
			` ${key.name}, built in ${key.buildYear}, is a ${key.streetSize} street`
		);
	});
	parkMap.forEach((key) => {
		if (key[3] > 1000) {
			console.log(` ${key[0]} has more than a 1000 trees`);
		}
	});
}

streetOutput();

const arr = [12, 54, 120, 66, 17, 35];

const sum = arr.reduce((prev, cur, index) => prev / cur, 1);

console.log(sum);

function codapec(x, y) {
	return [x / y, x * y];
}

const [mark, ruth] = codapec(12, 4);
