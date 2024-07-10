### Impact of a Data Breach:

**On the Company:**
> - Trust in the company declines, affecting its image and customer loyalty.
> - Costs arise from fixing the breach, paying fines, and recovering from operational disruptions.
> - Normal business operations are disrupted, resources are focused on addressing the breach.

**On Customers:**
> - Customers' personal information, like their bank information, could be stolen.
> - Customers feel their privacy is compromised.
> - Dealing with the aftermath can be stressful, as they have to change all of their passwords and dealing with the risks of the breach.

**To respond effectively:**
> - Organizations must first notify their users to prevent any more fraud.
> - Then, they must initiate a lockdown so no malicious users can login.
> - Investigating the breach and the perpetrator.
> - Remediation & Evaluation.
> - Managing Legal and Public Relations in order to prevent any more reputational damage.

---

- Write a Python script that reads a text file and counts the number of occurrences of each word. Describe how your script processes the file and counts the words.

```py
import string

# The file name
filename = 'sample.txt'

# For keeping track of every word's word count
word_count = {}

# Opening file
with open(filename, 'r', encoding='utf-8') as file:
    # Iterating through all the lines
    for line in file:
        # Making lines case insensitive
        line = line.lower().strip()
        # Removing punctuation cause we only want the words
        line = line.translate(str.maketrans('', '', string.punctuation))
        # Extracting the words from the lines using split()
        words = line.split()
        # Adding the word to the word_count counter list
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# Finally, printing the word, then the amount of times it showed up
for word, count in word_count.items():
    print(f'{word}: {count}')
```

---

- Explain the role of RAM in a computer system. What are its inputs and outputs, and how does it interact with the CPU and storage devices?

> **RAM** is like a computer's fast memory that holds onto data and instructions that are being used right now. It works closely with the CPU, which puts stuff into RAM for quick access and gets it back when needed. Unlike storage drives, RAM doesn't remember things once the computer is turned off. Its main job is to help the CPU work on things quickly while you're using your computer.

---

```sql
-- making the products table
create table products (
    product_id int primary key auto_increment,
    name varchar(100) not null,
    description text,
    price decimal(10, 2) not null
);

-- now for the customers
create table customers (
    customer_id int primary key auto_increment,
    name varchar(100) not null,
    email varchar(100) unique not null,
    address text
);

-- the orders
create table orders (
    order_id int primary key auto_increment,
    customer_id int,
    order_date date not null,
    total_amount decimal(10, 2) not null,
    foreign key (customer_id) references customers(customer_id)
);

-- finally, the orderdetails (to manage the many-to-many relationship between orders and products)
create table orderdetails (
    order_id int,
    product_id int,
    quantity int not null,
    primary key (order_id, product_id),
    foreign key (order_id) references orders(order_id),
    foreign key (product_id) references products(product_id)
);
```
**The result of the above has been saved into a .db file named `online_store.db`**

---

- Describe the concept of a VPN (Virtual Private Network). How does it work, and what are its advantages and disadvantages in terms of network security?

> A VPN is similar to a secret tunnel you can use to make your internet connection safer. It encrypts your data so others can't spy on what you're doing online. It also hides your real IP address, making it harder for websites to track you. VPNs are handy for staying safe on public Wi-Fi or accessing websites that might be blocked in your country. However, they can sometimes slow down your internet speed a bit and cost money to use. Some examples of these costly VPNs are NordVPN, Surfshark, CyberGhost and ExpressVPN

---

- Explain the concept of public key cryptography. Describe how it differs from symmetric key cryptography and provide an example of how it can be used to secure communication.

In **Public key cryptography**, Each person has a pair of keys: a **public key** for everyone to use and a **private key** kept secret. When someone sends a message, they use the receiver's public key to encrypt it. Only the receiver's private key can decrypt, or unlock, the message. This method is safer than **symmetric key cryptography**, where the **same key is used for both encryption and decryption.**

> For example, if Omar wants to send a secure message to Nasser, he uses Nasser's public key to encrypt it. Only Nasser, who has the matching private key, can decrypt and read the message, keeping their communication safe from others.

---

