# What's a Class?  _Why?_





You may already be an "old hat" at this whole _**Object-Oriented Programming**_ &  _**Class**_ thing -- especially if you are coming to Python from Java or Ruby.  If that's the case -- feel free to re-join the flow of this lecture for the Python-specific parts (multiple inheritance, meta classes, et. al.), & the exercises.  If your background is JavaScript , this might be a little weird at first, but hopefully not too confusing.



<br>



For the rest us, let's start at the beginning.


<br>


## Object Oriented Programming?


<br>


It might be simplest to think of **`OOP`** as a code  _organization technique_ - a way of sorting the pieces of a program into categories based on related data, qualities & capability.  If two different pieces of code do _mostly similar_ things to _mostly similar data_, their commonalities can be shared & reused instead of repeated.  Grouping data & functionality together for reuse in this way can make code cleaner, shorter, & more _modular_.

But since this is a programming class, let's get a little more formal:


<br>


**Wikipedia:**

> **Object-oriented programming** (**OOP**) is a [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm) based on the concept of "[objects](https://en.wikipedia.org/wiki/Object_(computer_science))", which may contain [data](https://en.wikipedia.org/wiki/Data), in the form of [fields](https://en.wikipedia.org/wiki/Field_(computer_science)), often known as *attributes;* and code, in the form of procedures, often known as *methods.* ...
>
>  ...There is significant diversity of OOP languages, but the most popular ones are [class-based](https://en.wikipedia.org/wiki/Class-based_programming), meaning that objects are [instances](https://en.wikipedia.org/wiki/Instance_(computer_science)) of [classes](https://en.wikipedia.org/wiki/Class_(computer_science)), which typically also determine their [type](https://en.wikipedia.org/wiki/Data_type).
>
> ...a **class** is an extensible program-code-template for creating [objects](https://en.wikipedia.org/wiki/Object_(object-oriented_programming)), providing initial values for state ([member variables](https://en.wikipedia.org/wiki/Member_variable)) and implementations of behavior (member functions or [methods](https://en.wikipedia.org/wiki/Method_(computer_programming)))


<br>

<br>


**Python Crash Course:** [**link**](https://nostarch.com/pythoncrashcourse)

> *Object-oriented programming* is one of the most effective approaches to writing software. In object-oriented programming you write *classes* that represent real-world things and situations, and you create *objects* based on these classes. **When you write a class, you define the general behavior that a whole category of objects can have.** When you create individual objects from the class, each object is automatically equipped with the general behavior; you can then give each object whatever unique traits you desire. You’ll be amazed how well real-world situations can be modeled with object-oriented programming. -- _**Python Crash Course**_


<br>

<br>


#### Feel like that's programming _buzzword bingo_? Here are a few definitions:


<br>
<br>


1.  **Paradigm** -- a classification, model, or philosophy.  A way of categorizing programming techniques or languages by feature.

3. **Class** -- "build instructions" describing some related data & functions for use in a program.
4. **Object | Instance** --  _one particular copy_ created from a Class.  A "working copy" with its own data & functions.  Object data (_state_) can _change_ separate from other Objects.  There can be many different Objects/Instances from one Class in use in a program.
5. **Instantiate |** (_construct_) -- _a fancy word for "create" or "bring into existence"_.   The process of  making an Object "working copy" from the Class"build instructions".  The code that does this is usually referred to as a _**`constructor`**_.
6. **self** -- a special keyword denoting data & methods that belong to an Object/Instance.  Data & methods intended for an Object always have _**self**_ as their first argument.
7. **property | attribute | _field_** -- Data stored in the Class/Object.  These variables can be data, multiple data structures, or  even instances of other Classes.  Properties with the prefix **self** are tied to an Object on instantiation & can be changed without effecting other Object copies made from the Class.
8. **method | function | _procedure_** -- the _related functions_ in the Class. Code that adds, deletes, or modifies the enclosed data &/or relates to the category & behavior of the Class.  Methods that take **self** as an argument are tied to an Object on instantiation & are usable on a per-Object basis (calling one Object's methods doesn't affect another Object made from the Class).



<br>



#### _Other ways of thinking about Classes?_ Template, schematic, blueprint.


<br>
<br>
<img width="80%" alt="Classes are Blueprints for Objects" src="/images/blueprint to house.png">
<br>
<br>


#### Anatomy of a Class in Python


<br>
<br>
<img alt="Anatomy of a Class in Python" src="/images/anatomy of a class.png">
<br>
<br>



You can interact with this code example [**here**](https://trinket.io/python3/a513716e54).  Or click **Code Snippet** below for a **snippet** you can cut and paste into your editor.


<details>
<summary>Code Snippet</summary>



```python

import datetime

class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
​                     levels=1, bathrooms=2, bedrooms=2,
​                     kitchen={'Island':False, "Pantry": True, "oven": True, "Stove": "Gas"},
​                     livingroom={"Fireplace": False, "Bay Windows": False, "Window Coverings": "Blinds"},
​                     diningroom=True, basement=False):
​
      self.build_date=build_date
      self.levels=levels
      self.bathrooms=bathrooms
      self.bedrooms=bedrooms
      self.kitchen=kitchen
      self.livingroom=livingroom
      self.diningroom=diningroom
      self.basement=basement
      self._property_value=0
      self._markup=.20
      self.taxes=0.0


  @property
  def list_price(self):
    price = (self._property_value * self._markup + self._property_value)
​
    return f'${price:,.2f}'

  @list_price.setter
  def list_price(self, amount):
    self._property_value=amount / (self._markup + 1)

  def is_new(self):
    return self.build_date > datetime.date(2010, 11, 15)
​
  def have_party(self):
    print("We're having a party!!")


#making a fresh, new BaseHouse instance called 'my_house'
my_house = BaseHouse(levels=2, basement=True)

#__dict__ lists this ojects attribute dictionary
print(my_house.__dict__)

#calling is_new() method
print(my_house.is_new())

#setting the list_price attribute
my_house.list_price = 400000

#retrieving the list_price
print(my_house.list_price)
​
```


</details>
<br>
<br>


## What's the OOP Upside?



<br>



Object-oriented programming can have many benefits -- the biggest being conceptual shorthand for modeling the 'real world' in code.  But _formally?_  OOP has four principles, that help explain the programming advantages:  **`encapsulation`, `abstraction`, `inheritance`, & `polymorphism`**.


<br>
<br>


####  1:  `Encapsulation`
 _**I stay out of your business, & you stay out of mine.**_

 An Objects properties (_data_) are "walled off"_ from other code.  Anything interacting with an Objects properties must do so by _explicitly asking_ -- (e.g., calling the attribute through (dot) notation, or using the Objects methods*.)

 With **`encapsulation`**, it becomes harder for code in one place in the program to accidentally interfere with code another part  -- or mutate data it doesn't have permission for.

 *<sub>If you're coming from Java, you'll find that all attributes are **`public`** in Python...but you can still flag them as "managed".  See [**this**](https://docs.python.org/3/tutorial/classes.html#private-variables) for a detailed explanation.  **`@property`** & **`@property.setter`** in the example code are part of this mechanism.</sub>


<br>


#### 2:  `Abstraction`

 _**You interact with me using a general definition of what kind of thing I am.**_

  Essential functions are represented without specifics.  _**How**_ I fulfill the definition is up to me (_implementation details_),  as long as I continue to give you what you need according to the general definition.

  Applying abstraction to unit of code means _**only**_ exposing a _**high-level**_ mechanism for using it.  That sounds _almost identical_ to encapsulation.  But :   **`encapsulation`**  == _**data**_ isolation.  **`abstraction`** == _**implementation**_ isolation.




<img src="/images/Abstract cars.png" width="80%" alt="cars in the abstract" >



 <sub>**e.g**. - Cars are things that have 4 wheels.  They're _**drivable**_:  they **move**, **shift**, & **break**. Lower-level details of the engine  (_electric, hybrid, gas, or diesel?_), the breaks (_drum, disc, anti-lock, emergency_), or the transmission (_automatic, dual clutch, direct shift gearbox_) aren't important.  If my vehicle qualifies as a _**Car**_, it will have 4 wheels & methods to _**move, shift, & break**_.  It will be _**drivable**_. </sub>



<br>



#### 3:  `Inheritance`

_**No need to make your own version if you can borrow from someone else.**_

Classes provide an _organizational unit for **reuse** through **`inheritance`**_.  "Child" classes automatically get access to all the data & functions defined inside their designated "Parent".

  _**`Inheriting`**_ general code from a Parent allows you to focus on adding only the  _more specialized_ code & data needed for your use case. Children can also alter or _override_ Parent methods -- if (say) the behavior you're implementing is only 80% similar.


<br>
<br>
<img width="80%" alt="Inheritance example with house blueprints" src="/images/blueprint inheret.png">



 <sub>**i.e.** You create a _child_ Class that _derives_ from a _parent_ Class (the common or more general functionality), & then add functions that implement what you need to accomplish.</sub>


<br>
<br>



#### The Anatomy of a Child Class



<br>
<br>
<img alt="Anatomy of a child class" src="/images/Child Class.png">
<br>


You can interact with this code sample [**here**]().  Or click **Code Snippet** below to get a **snippet** you can copy & paste into your editor.



<details>
<summary>Code Snippet</summary>


​
  ```python

import datetime

#Here is the child, inheriting from BaseHouse.
#Note 'BaseHouse' goes in the paretheses.
class FancyHouse(BaseHouse):
  def __init__(self, build_date=datetime.date(2012, 4, 13),
​                     levels=2, bathrooms=2, bedrooms=3,
​                     kitchen={'Island':True, "Pantry": True,
                               "oven": True, "Stove": "Gas"},
​                     livingroom={"Fireplace": True, "Bay Windows": True,
                                  "Window Coverings": "Drapes"},
​                     diningroom=True, basement=False,
                      pool="above-ground", poolhouse=True):
​
    #Here we call the parent constructor and pass it
    #all the arguments for the inhereted properties.Note the lack of the self keyword.
    super().__init__(build_date, levels, bathrooms, bedrooms,
                     kitchen, livingroom, diningroom, basement)

    #Here, the child adds two more attributes on top of the inhereted attributes.
    self.pool=pool
    self.poolhouse=poolhouse


  @property
  def list_price(self):
​    price = (self._property_value * self._markup + self._property_value)
​
    return f'${price:,.2f}'

  @list_price.setter
  def list_price(self, amount):
​    self._property_value=amount / (self._markup + 1)

  def is_new(self):
​    return self.build_date > datetime.date(2010, 11, 15)
​
  def have_party(self):
​    print("We're having a party!!")

  #new method unique to the child class
  def have_swim_party(self):
​    print("We're swimn' and chillin'.  It's a Party!")

  #another method unique to the child class
  def host_guests(self, guests):
​    if self.poolhouse:
​      print(', '.join(item for item in guests) + "... staying in the poolhouse." )
​    else:
​      print(', '.join(item for item in guests) + "... staying in the spare bedroom.")
​
​
track_house= BaseHouse()
your_house= FancyHouse()
my_house=FancyHouse(poolhouse=False)


#The attribute dictionaries for all our objects.
#This is from the parent.  Note the absence of the pool and poolhouse
print("Track House attributes: ", track_house.__dict__)
print("___________________")

#This is from the child class.
#Note the pool and pollhouse
print("Your House attributes: ", your_house.__dict__)
print("___________________")

#This object "turned off" the poolhouse option on the child.
print("My House attributes: ", my_house.__dict__)
print("___________________")


#Calling the party method from the parent
my_house.have_party()
print("___________________")
#Calling the added methods from the child class
your_house.have_swim_party()
your_house.host_guests(["Bob", "George", "Mary"])
print("___________________")
#Note that the conditional logic triggers here, because
#"my_house" doesn't have a poolhouse.
my_house.host_guests(["Bob", "George", "Mary"])
​
  ```


​<br>
<gr>
</details>
<br>

<br>



#### 4:  `Polymorphism`* --  _"Greek for `'many shapes'` "_.

 _**“When I see a bird that walks like a duck .... & quacks like a duck, I call that bird a duck.” (James Whitcomb Riley)**_.

 Very generally, **`polymorpic`**  Classes have identically named functions --  _**implemented differently**_ , fulfilling common _**use cases**_ (also called _**interfaces**_).

 Each Class' function fulfills the interface in its own way -- but _outside_ code can _**use**_ or _**call**_ the function based on the general, shared expectations (_interface_).

**`polymorphic Classes`** can be _derived_ or completely separate.  With the inheritance version, _child_ Classes re-implement an _inherited function_ while allowing outside code to use _either_ the child's  or parents function interchangeably.



<br>
<img width="45%" src="/images/poly drive.png">
<br>


<sub>e.g. -- Using our previous **drive** example  --  now we have a delivery Truck & a Surf Van.  Both _**drive**_ - except they're _**not**_ classified as cars.  But for our **use**, we don't care that these aren't cars...only that they're _**drivable**_.   If they're _**drivable**_ -- we can use them they way we'd use a car. Here is an excellent [**extended explainer**](https://www.digitalocean.com/community/tutorials/how-to-apply-polymorphism-to-classes-in-python-3) from Lisa Tagliaferri @ DigitalOcean.</sub>


<br>

Put another way...
> You're in the middle of a large room, when a zombie shuffles out of hiding & comes at you.  You're unarmed.
>
> Lucky for you, your friend is standing in the doorway.
>
> **"Quick!  Throw me something I can bash the zombie with!!"** you shout to her.
>
>
>
> ...you weren't specific (you really don't care) about **_what_** -- as long as it's _**thrown to you**_ & it's something that you can use (pickup or trigger) to  _**bash zombies**_ (weapon).

.....& a funny example (paraphrased from [**Stack Overflow**](https://stackoverflow.com/questions/2866987/what-is-the-definition-of-interface-in-object-oriented-programming))



<br>

<br>

<img align="left" width="60" src="/images/package.png">
<p vertical-align="middle"><h3>&nbsp; Wrapping it Up</h3></p>

<br>

<br>

So we've gone a little into _**What**_ a Class is, & _**why**_ you might want to use one in your code.  But this stuff is complex, so in the [**next section**](./classesinpython.md), we'll go over making and using classes in detail, to give you some concrete practice.
