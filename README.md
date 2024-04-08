# Python-Exercises
Handling and use of functions with arrays
2.1.1. You are required to make a modularized program (using functions and error handling) that allows you to
to move the letter P into an MxN matrix, where M (Number of rows) and N (Number of columns) are values entered by the user.
values entered by the user.

2.1.2. The letter X will have as initial position (x, z) where x corresponding to the rows is entered by the user and z corresponding to the columns is entered by the user.
and z corresponding to the columns is also entered by the user. The other positions must
contain 0.

2.1.3. The P will move within the matrix, but it can never go out of the established limits which are (0, 0) and
(M, N). To move the P in the matrix must be done by taking as a basis the values contained in the following vector v: v = 1.
the following vector v: v = 1, -1, 2, 2, 3, -1, 2, 1, 1, 0.

2.1.4. Each value of the vector v will add or subtract the number of positions in the matrix according to its sign.

2.1.5. The positions move in row and column as follows:

2.1.5.1. The first position moves down if the value is negative, and moves up if the value is positive.
positive.

2.1.5.2. The second position moves to the left if the value is negative, and to the right if it is positive.
positive.
2.1.5.3. It starts again as in 2.1.5.1.

2.1.6. Each time P is moved the previous position must change to 0.

2.1.7. The initial matrix must be printed and then after each movement. It should be printed as follows
below:

For a 3x3 matrix with initial position 0, 1

[ 0, P, 0]
[ 0, 0, 0]
[ 0, 0, 0]

2.2. Develop a modular program with OOP that satisfies the following:

The clinical laboratory, Konoha SAS, is interested in recording the laboratory tests it performs on patients.
patients.

The patients may belong to a health entity that covers the exams, they may be users of a health policy or be individuals.
users of a health insurance policy or be individuals. In all cases of patients, you are interested in knowing
number and type of identification, first and last names, date of birth, cellular phone number, e-mail, name of another person to contact
email, name of another person to contact and contact telephone number.

When a patient arrives requesting tests to be performed, if he/she is not registered, all the data is requested and recorded in the system.
the system, and with the order sent by the physician, the exams are registered.
exams. An order must be created in the system, this order must have a consecutive number, date of request, date of entry into the system
This order must have a consecutive number, date of request, date of entry in the system, treating physician and number of the order given by the physician.
The next step is to enter the tests requested by the physician: type of test (CUM code), date of performance and observations.
The exams can be one or several.

The following information is handled from the physician: ID card, first and last names, cell phone number, address, professional card number,
address, professional card number.

For private patients only, an invoice must be created for each order of exams performed.
must have invoice number, value to be paid, patient information (ID card, full name, address, phone number), date of invoice
address, telephone number), date of creation of the invoice. Each type of exam has a different value.
different, for example, the value of a triglyceride test is 15.000, a simple hemogram is 10.000, etc.
10,000, etc.

At the end of the month, an invoice must be generated, related to the different orders of the provider entity that will pay for the
the provider that is going to pay for the examinations. It is possible to consult, by invoice number, the header of the invoice
of the invoice with the details of the exams that were performed (type of exam, order number, patient's ID number) and the total value of the exams,
patient's ID) and the total value of the invoice.

At the end of the month, it is of interest to know the treating physician who referred the most patients. A consolidation of
by type of patient (individual or by health entity), ordered from highest to lowest. Also
information is also required for a particular patient (by ID number), what tests he/she underwent and the date they were performed.
performed with date of performance.

From the health care providers, we would like to know NIT, contact telephone numbers, cell phone number, e-mail, name of another person to contact and contact telephone number, and type of health care provider.
contact name and telephone number, and type of provider entity (Contributive Regime, Prepaid, Subsidized Regime, etc.).
(Contributive Regime, Prepaid, Subsidized Regime).
