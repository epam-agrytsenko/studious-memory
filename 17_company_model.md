
##### Company model


Using OOP, it is necessary to model the interaction between a company and its employees.

Pay attention to the file [utils/business.py](utils/business.py). It contains some templates that need to be implemented.

### Implement the following model:

###### Class `Company`
 * The company has a name and an address.
 * The company has a list of employees (`employees`).
 * Only managers or engineers can become employees of the company.
 * The company can dismiss any employee.
 * The starting capital of the company is 1000 coins (`money`).
 * The company pays its employees for their work.
 * When the company has a holiday, each employee receives 5 coins.
 * When the company runs out of money, it goes bankrupt, and all its employees become unemployed.

###### Class `Person`
 * A person has a name and an age. An address and gender can also be specified.
 
###### Class `Employee` (base class for employees, inherits from Person)
 * An `employee` can be hired by a company or be unemployed.
 * An `employee` can only work in one company.
 * An `employee` cannot work if they are unemployed.
 * The starting capital of an `employee` is 0 coins.
 
###### Class `Engineer` (inherits from Employee)
 * An engineer earns 10 coins for their work. The money is deducted from the company's balance and added to the engineer.
 
###### Class `Manager` (inherits from Employee)
 * A manager earns 12 coins for their work. The money is deducted from the company's balance and added to the manager.

---