# Classes in Python



### What's a Class, again?

Let's recap with a quote from the Python docs:



> _Classes provide a means of bundling data & functionality together. Creating a new class creates a new *type* of object, allowing new *instances* of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state. -- [**Python Docs: Classes**](https://docs.python.org/3/tutorial/classes.html)_



**Classes:  Templates for data & the code that operates on (or relates to) the data.**  Reusable containers for data & linked functions. -- _Tupperware containers with Snacks & utensils inside.  Blueprints with options.  Templates with instructions._ You get the picture.



### Inner Workings


<br>
<br>
<img width="75%" alt="declaring a class image" src="/images/declareaclass.png">
<br>
<br>




#### Classes are declared using the `class` keyword, followed by the **`ClassName`**, and a **`:`**.


<br>

Only include **(parentclass)** when **extending** or **inheriting** from Parent class(es).  Methods & attributes are declared _inside the class body (**indicated by indentation**)_.   Attributes & methods that apply individually to Objects made from the Class require the **`self`** keyword.

You can interact with the code examples in the sections below [**here**](https://trinket.io/python3/bf6cb9118a)


<details>
<summary>Code Snippet</summary>



```python
  class HouseCat:
      def __init__(self, size, color, fur, name):
          self.hunger = 0
          self.tired = 0
          self.size = size
          self.color = color
          self.fur = fur
          self.name = name

      def eat(self, food):
        if self.hunger > 5:
          print(f"Mmmmmmm {food}!  Is good.")
          self.hunger -= 1
        elif self.hunger > 0:
          print(f"Humph. Eats {food}, I guess.")
          self.hunger -= 1
        else:
          print(f"YUCK!  {food} gross.  No eats.")


      def play(self, toy):
        if self.tired >= 5:
          print("Come back later, human.  I's tired.")

        elif self.tired > 1:
          print(f"Eh - I's follow the {toy} and *observe*.")
          self.tired += 1
        else:
          print(f"I's chase the {toy}! I's chase it!!")
          self.tired +=2

      def talk(self):
        return "PURR PURR"


      def what_kind(self):
        return " ,".join((self.size, self.color, self.fur))

```

<br>
<hr>
</details>


<br>
<br>



####  **`instantiate`** an **`Object`** from a Class by typing `ClassName()`


<br>


Pass any _**arguments**_ required by the **`__init__`** function into the **`()`** after Class Name.


<details>
<summary>Code Snippet</summary>



```python
#Making Object george, an instance of HouseCat
george = HouseCat("Lg", "Tabby", "Longhair", "George")

#Making Object buttercup, a different instance of HouseCat
buttercup = HouseCat("small", "Black", "Shorthair", "Buttercup")

#buttercups stats
print(buttercup.what_kind())
>>> "small, Black, Shorthair"

#georges stats
print(george.what_kind())
>>> "Lg, Tabby, Longhair"


```

<hr>
</details>
<br>
<br>



#### Refer to the **`attributes`** &  **`methods`**of an Object by using **`dot notation`**.


<details>
<summary>Code Snippet</summary>



```python
buttercup.eat("Tuna")
>>> "YUCK!  Tuna gross.  No eats."

george.eat("Trout")
>>> "YUCK!  Trout gross.  No eats."

george.play("mouse")
>>> "I's chase the mouse!  I's chase it!!"

buttercup.play("red light")
>>> "I's chase the red light!  I's chase it!!"

buttercup.play()
>>> "Eh - I's follow the red light and *observe*."

print(george.tired)
>>>2

print(buttercup.tired)
>>>3

```



<hr>
<br>
</details>
<br>
<br>



#### Class Attributes are _Shared_ across Instances (Objects)

You can interact with the code examples in the sections below [**here**](https://trinket.io/python3/b672d82dab)



<details>
<summary>Code Snippet</summary>



```python
class HouseCat:
      #These three attributes belong to the *Class*, and are shared across Objects
      legs = 4
      eyes = 2
      ears = 2

      #Construtor for individual Objects.  These attribute values vary by Object.
      def __init__(self, size, color, fur, name):
          self.hunger = 0
          self.tired = 0
          self.size = size
          self.color = color
          self.fur = fur
          self.name = name

      def eat(self, food):
        if self.hunger > 5:
          print(f"Mmmmmmm {food}!  Is good.")
          self.hunger -= 1
        elif self.hunger > 0:
          print(f"Humph. Eats {food}, I guess.")
          self.hunger -= 1
        else:
          print(f"YUCK!  {food} gross.  No eats.")


      def play(self, toy):
        if self.tired >= 5:
          print("Come back later, human.  I's tired.")

        elif self.tired > 1:
          print(f"Eh - I's follow the {toy} and *observe*.")
          self.tired += 1
        else:
          print(f"I's chase the {toy}! I's chase it!!")
          self.tired +=2

      def talk(self):
        return "PURR PURR"


      def what_kind(self):
        return ", ".join((self.size, self.color, self.fur))


george=HouseCat("Lg", "Tabby", "Longhair", "George")
buttercup=HouseCat("small", "Black", "Shorthair", "Buttercup")


#Note that the class attributes aren't listed in the Object attributes list
#Because the values are *shared*
print("Buttercup attributes: \n", buttercup.__dict__)
print("-----------------------")
print("George attributes: \n", george.__dict__)
print("-----------------------")

#Here are the Class Attributes
print("HouseCats attributes: \n", HouseCat.__dict__)
print("-----------------------")


#Both George and Buttercup have 2 ears
print("Georges ears: ", george.ears)
print("Buttercups ears: ", buttercup.ears)

#Now we change how many ears *all* HouseCats have
HouseCat.ears = 1.5

#And *both* HouseCats Change as a result
print("Georges ears: ", george.ears)
print("Buttercups ears: ", buttercup.ears)
print("\n\n")


#Here are the changed Class Attributes
print("HouseCats attributes: \n", HouseCat.__dict__)
print("-----------------------")

```


<hr>
<br>
</details>
<br>
<br>



#### Use **`property()`**  &   **`@property`** to more closely  manage & protect Object **`attributes`** with _**getters**_ & _**setters**_


<br>



Remember _**encapsulation**_?  While Python doesn't have a _**private**_ keyword (like Java does) to stop code from outside a Class changing attributes, it does provide a convention for _managed attributes_.

Read-only (_managed_) Object attributes are denoted using a **`_`** prefix.  Access (a _getter_) to the attribute is then provided with the _**`@property`**_  decorator.

_Setters_ & _deleters_ (if needed) can be provided through _`@propertyname.setter`_ and_`@propertyname.deleter`_.

For more details, see [**the Python Docs here**](https://docs.python.org/3/library/functions.html#property).

You can interact with this code sample [**here**](https://trinket.io/python3/cd5db23be2)



<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

class SimpleHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13)):

    #These are the "regular" Object properties
    self.build_date=build_date
    self.levels=1
    self.bathrooms=2
    self.bedrooms=2
    self.taxes_paid=False

    #These are the properties I want to flag as "managed" or "private"
    self._property_value=100000.00
    self._markup=.20
    self._tax_rate=.0136


  #Here, property_value is returned as a regular-looking property of the Object
  #HOWEVER, without a setter (commented out below), you can't change this property.
  @property
  def property_value(self):
    return self._property_value

  '''
  @property_value.setter
  def property_value(self, value):
    self._property_value = value
  '''

  @property
  def taxes(self):
     return (self._property_value * self._tax_rate)


  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.taxes
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")




#making a fresh, new SimpleHouse instance called 'my_house'
my_house = SimpleHouse(build_date=datetime.date(2015, 5, 16))

#__dict__ lists this ojects attribute dictionary
print(my_house.__dict__)

#this *gets* the property named "property_value"
#by retrieving the managed property "_property_value"
print(my_house.property_value)

#nice taxes
print(my_house.taxes)

#this will toss an error, because there is no *setter* for property_value
my_house.property_value = 400000

########################################

#Now, un-comment the setter
my_house.property_value = 400000

#Now, we can see that we've changed the property_value
print(my_house.property_value)

#And our taxes went up
print(my_house.taxes)
```



<br>
<hr>
</details>
<br>
<br>



#### `@property` Can be Used to Combine & Jointly Manage Read-Only Properties



<br>



You can provide an extra layer of management by combining individual read-only attributes into one property.  The setter for the **`@property`** can then change both the underlying attributes.

You can interact with this code sample [**here**](https://trinket.io/python3/3483aae7c4)


<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

class SimpleHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13)):

    self.build_date=build_date
    self.levels=1
    self.bathrooms=2
    self.bedrooms=2
    self.taxes_paid=False

    #These are the properties I want to flag as "managed" or "private"
    self._property_value=100000.00
    self._markup=.20
    self._tax_rate=.0136


  #Here, we have the notion of a *list_price* that is a combination
  #of _property_value and _markup.
  @property
  def list_price(self):
    price = (self._property_value * self._markup + self._property_value)

    return f'${price:,.2f}'

  #Here, we provide a way of setting the list price and thereby
  #Re-calculating & setting the _property_value, by subtracting the _markup.
  @list_price.setter
  def list_price(self, amount):
    self._property_value = amount / (self._markup + 1)


  #Here, we have taxes calculated on the _property_value
  @property
  def taxes(self):
     return (self._property_value * self._tax_rate)


  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.taxes
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")



#making a fresh, new SimpleHouse instance called 'new_house'
new_house = SimpleHouse(build_date=datetime.date(2017, 2, 20))

#__dict__ lists this ojects attribute dictionary
print(new_house.__dict__)

#getting the taxes based on the defalut _property_value of 100k
print(new_house.taxes)


#retrieving the current list_price
print(new_house.list_price)


#changing the list_price (and thus, the _property_value)
new_house.list_price = 450000


#checking if the taxes went up.  They did.
print(new_house.taxes)

```


<hr>
<br>
</details>
<br>
<br>



### Use **`@classmethod`** for Methods that Belong to the Whole Class



<br>



As with _**Class attributes**_, Class _**methods**_ apply to the _whole Class_, & do not require an instance.  They also cannot change individual Object data.  They take _**`cls`**_ (the Class) as their first parameter, & have the _**`@classmethod`**_ decorator.  A common use for _**`classmethods`**_ is to provide alternative _**constructors**_ (_factories_) for Objects that pre-set various attributes.

You can interact with this code sample [**here**](https://trinket.io/python3/57fd47b861)


<details>
<summary>Code Snippet</summary>



```python
import datetime

class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
               levels=1, bathrooms=2, bedrooms=2,
               kitchen= {'Island':False, "Pantry": True,
                        "oven": True, "Stove": "Gas"},
               livingroom= {"Fireplace": False, "Bay Windows": False,
                           "Window Coverings": "Blinds"},
               diningroom=True, basement=False):

    self.build_date=build_date
    self.levels=levels
    self.bathrooms=bathrooms
    self.bedrooms=bedrooms
    self.kitchen=kitchen
    self.livingroom=livingroom
    self.diningroom=diningroom
    self.basement=basement
    self._property_value=10000
    self._markup=.20
    self.taxes=0.0

  #A Classmethod that makes a default BaseHouse, but with 2 levels
  @classmethod
  def two_story(cls):
    return cls(levels=2)

  #A Classmethod that makes a BaseHouse with 3 levels
  @classmethod
  def three_story(cls):
    return cls(levels=3, basement=True)

  #A Classmethod that makes a 3 bedroom
  @classmethod
  def three_bedroom(cls):
    return cls(bedrooms=3)

  #A Classmethod that makes a fancy livingroom.  Note the added Ceilings.
  @classmethod
  def fancy_livingroom(cls):
    return cls(livingroom={"Fireplace": True, "Vaulted Ceilings":True,
                           "Bay Windows": True, "Window Coverings": "Drapes"})

  #For printing out a representation of the class.
  def __str__(self):
    return "house specs are:  \n\n" + "\n".join([item[0] + ": " + str(item[1])
                                                 for item in self.__dict__.items()])



#making a fresh, new BaseHouse instance called 'my_house',
#keeping the default args already in the __init__
my_house = BaseHouse()


#making a prefab house with defaults but three bedrooms
#by calling the *three_bedroom* Class method
your_house = BaseHouse.three_bedroom()

#The attributes from the default house
print("The 'my_house' " + my_house.__str__())
print("___________\n\n")

#The attributes from the three_bedroom method
print("The 'your_house' " + your_house.__str__())
print("___________\n\n")

#And here we order up one with a fancy_livingroom.
#Note the added Valuted Ceilings.
doodle = BaseHouse.fancy_livingroom()
print("The 'doodle' " + doodle.__str__())
```



<hr>
<br>
</details>
<br>
<br>



### Use **`@staticmethod`** for helper Methods in the Class that are related but not directly connected.



<br>



_**`@staticmethods`**_ work like "regular" Python functions, but they belong to (& can be called from ) _either_ the _Class' namespace_ or an _Objects namespace_.  They work _without_ making an Object.  They're most commonly used to group together functions that have a logical _connection_ to the Class or its data -- but they don't require _access_ to it.

  _**`@staticmethods`**_ cannot directly modify either Class or Object state (they don't take **`cls`** or **`self`** as parameters), but _do_ need to be called using either the Class _name_ or the Object _name_.

You can interact with this code example [**here**](https://trinket.io/python3/588e3ed0b4)


<br>
<details>
<summary>Code Snippet</summary>



```python
import random
from collections import defaultdict

#This is a Caretaker utility class.
#It has both attributes and methods for Caretakers
#And also static methods for outside use.
class Caretaker:
  def __init__(self):
    self.cats=defaultdict(int)
    self.food=defaultdict(int)
    self.toys=defaultdict(int)


  def buy_food(self, food):
    for item in food:
      self.food[item] += 1


  def buy_toys(self, toys):
    for item in toys:
      self.toys[item] +=1



  #You can adopt a random cat without having a caretaker
  @staticmethod
  def adopt_random_cat():

    sizes = ["xSm", "Small", "Medium", "Large", "xLg", "tiny", "xxLg"]
    hair =  ["hairless", "short", "long", "xlong", "med"]
    color = ["tabby", "black", "brown", "grey", "tortishell", "orange stripe", "grey stripe", "white"]
    name =  ['Grammercy', 'Leopold', 'Francis', 'George', 'Betty', 'Tabitha', 'Buttercup', 'Coco', 'Leisel', 'Greta', 'Bunnie', 'Walter']

    return HouseCat(random.choice(sizes), random.choice(color), random.choice(hair),  random.choice(name))


  #You can feed a cat without having a seperate caretaker
  @staticmethod
  def feed(cat, food):
    if not isinstance(cat, HouseCat):
      print("Ooops, you can't feed that, it's not a cat!")
    else:
      cat.eat(food)

  #anyone can play with a cat
  @staticmethod
  def play_with(cat, toy):
    if not isinstance(cat, HouseCat):
      print("I don't think you should be playing with that.  It's not a cat.")
    else:
      cat.play(toy)


#here is our HouseCat Class
class HouseCat:

    def __init__(self, size, color, fur, name):
        self.hunger = 0
        self.tired = 0
        self.size = size
        self.color = color
        self.fur = fur
        self.name = name

    def eat(self, food):
      if self.hunger > 5:
        print(f"Mmmmmmm {food}!  Is good.")
        self.hunger -= 1
      elif self.hunger > 0:
        print(f"Humph. Eats {food}, I guess.")
        self.hunger -= 1
      else:
        print(f"YUCK!  {food} gross.  No eats.")


    def play(self, toy):
      if self.tired >= 5:
        print("Come back later, human.  I's tired.")

      elif self.tired > 1:
        print(f"Eh - I's follow the {toy} and *observe*.")
        self.tired += 1
      else:
        print(f"I's chase the {toy}! I's chase it!!")
        self.tired +=2


#Making kitties
buttercup=HouseCat("small", "Black", "Shorthair", "Buttercup")
george=HouseCat("Lg", "Tabby", "Longhair", "George")


#Anyone can feed a cat by using the Caretaker staticmethod feed()
Caretaker.feed(buttercup, "Salmon")
Caretaker.play_with(george, "Butterfly stick")

print("___________________\n")

#Anyone can adopt a random(ish) cat using Caretaker.adopt_random_cat
new_kitty = Caretaker.adopt_random_cat()
print(new_kitty.__dict__)

print("___________________\n")

#But we can make a specific caretaker, who can buy food
ruby=Caretaker()
ruby.buy_food(["Tuna", "Salmon", "Trout"])
print(ruby.food)

print("___________________\n")
#And that specific Caretaker can also play with & feed cats
ruby.play_with(george, "red light")
ruby.feed(george, "Tuna")
```



<hr>
<br>
</details>
<br>
<br>



#### Child Classes are declared using the `class` keyword, followed by the **`ClassName`**, the **`(ParentName)`**and a **`:`**.



<br>



The **`ChildClassName(ParentClassName):`** pattern is used when **extending** or **inheriting** from Parent class(es).  All attributes & methods from the Parent(s) are accessible from the Child class without having to re-implent them.*  The Child class can then add its own more specific functions & data as needed.

<sub>*There's a little bit of an exception here for @property that we'll cover in a little bit.</sub>

You can interact with this code snippet [**here**](https://trinket.io/python3/f8d166fcd2)


<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
                     levels=1, bathrooms=2, bedrooms=2,
                     kitchen={'Island':False, "Pantry": True, "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": False, "Bay Windows": False, "Window Coverings": "Blinds"},
                     diningroom=True, basement=False):

    #These are the "regular" Object properties,
    #set by the args passed into the constructor
    self.build_date=build_date
    self.levels=levels
    self.bathrooms=bathrooms
    self.bedrooms=bedrooms
    self.kitchen=kitchen
    self.livingroom=livingroom
    self.diningroom=diningroom
    self.basement=basement
    self.taxes_paid=False

    #managed attributes
    self._property_value=100000.00
    self._markup=.20
    self._tax_rate=.0136


  @property
  def property_value(self):
    return self._property_value

  @property
  def list_price(self):
    price = (self._property_value * self._markup + self._property_value)

    return f'${price:,.2f}'

  @property
  def taxes(self):
     return (self._property_value * self._tax_rate)

  @property_value.setter
  def property_value(self, value):
    self._property_value = value


  @list_price.setter
  def list_price(self, amount):
    self._property_value=amount / (self._markup + 1)


  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.taxes
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")

  def is_new(self):
    return self.build_date > datetime.date(2010, 11, 15)

  def have_party(self):
    print("We're having a party.  WOOT!")


  #For printing out a representation of the class.
  def __str__(self):
    return "house specs are:  \n\n" + "\n".join([item[0] + ": " + str(item[1]) for item in self.__dict__.items()])



#Here is the child, inheriting from BaseHouse.
class FancyHouse(BaseHouse):

  #Note that the default args are mostly the same (values are different tho.)
  #The child *adds* arguments for additional child attributes.
  def __init__(self, build_date=datetime.date(2015, 6, 13),
                     levels=2, bathrooms=3, bedrooms=3,
                     kitchen={'Island':True, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": True, "Bay Windows": True,
                                 "Window Coverings": "Drapes",
                                 "Vaulted Ceilings": True},
                     diningroom=True, basement=False, lot=21780,
                     pool="in-ground", poolhouse=True):


    #Here we call the parent constructor and pass it all inhereted properties arguments
    #to avoid overwriting Parent-defined attribues with a different child version, since
    #we extended the Parent __init__.
    #Note the use of *super()* and the lack of the *self* keyword.
    super().__init__(build_date, levels, bathrooms, bedrooms,
                     kitchen, livingroom, diningroom, basement)

    #Here, the child adds its attributes on top of the inhereted attributes.
    self.pool=pool
    self.poolhouse=poolhouse
    self.lot=lot


  #new method unique to the child class
  def have_swim_party(self):
    print("We're swimn' and chillin'.  It's a Party!")


  #another method unique to the child class
  def host_guests(self, guests):
    if self.poolhouse:
      print(', '.join(item for item in guests) + "... staying in the poolhouse." )
    else:
      print(', '.join(item for item in guests) + "... staying in the spare bedroom.")


track_house= BaseHouse()
your_house= FancyHouse()
my_house=FancyHouse(poolhouse=False, lot=10000, basement=True, pool="above-ground")


#The attributes for all our objects.
#This Object is made from the parent.  Note the absence of the pool & poolhouse
print(track_house.__str__())
print("___________________")

#This Object is made from the child class.
#Note that we're calling the method definied in the Parent,
#but get the Childs properties - pool, pollhouse, etc.
print(your_house.__str__())
print("___________________")

#This Child Object "turned off" the poolhouse option, and has other differences.
print(my_house.__str__())
print("___________________")
print("___________________")

#Calling the Parent Party Method on the Child
my_house.have_party()


print("___________________")
#Calling the added methods from the child class
your_house.have_swim_party()
your_house.host_guests(["Bob", "George", "Mary"])
print("___________________")

#Note that the conditional logic triggers here, because
#"my_house" doesn't have a poolhouse.
my_house.host_guests(["Bob", "George", "Mary"])

#Note that the Object from the Parent Can't have a swim Party
track_house.have_swim_party()


>>>Traceback (most recent call last):
  File "/tmp/sessions/ec1f1e52de305acf/main.py", line 146, in <module>
    track_house.have_swim_party()
AttributeError: 'BaseHouse' object has no attribute 'have_swim_party'
```


<hr>
<br>
</details>
<br>
<br>



#### **`ParentClassName`** can include a _module_ or _library_ name, if the Parent class is not in the same scope or file as the Child Class.  e.g. **`ChildClassName(modulename.ParentClassName)`**


You can interact with this code snippet [**here**](https://trinket.io/python3/f8d166fcd2)


<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime, dwellings

#Here is the child, inheriting from dwellings.BaseHouse.
class FancyHouse(dwellings.BaseHouse):
  def __init__(self, build_date=datetime.date(2015, 6, 13),
                     levels=2, bathrooms=3, bedrooms=3,
                     kitchen={'Island':True, "Pantry": True, "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": True, "Bay Windows": True, "Window Coverings": "Drapes", "Vaulted Ceilings": True},
                     diningroom=True, basement=False, lot=21780, pool="in-ground", poolhouse=True):

    super().__init__(build_date, levels, bathrooms, bedrooms, kitchen, livingroom, diningroom, basement)

    self.pool=pool
    self.poolhouse=poolhouse
    self.lot=lot


  def have_swim_party(self):
    print("We're swimn' and chillin'.  It's a Party!")


  def host_guests(self, guests):
    if self.poolhouse:
      print(', '.join(item for item in guests) + "... staying in the poolhouse." )
    else:
      print(', '.join(item for item in guests) + "... staying in the spare bedroom.")


#here, we have to use the module name to instantiate a Parent Object
track_house= dwellings.BaseHouse()

#here, we don't have to, becasue our Child did it for us in the Class statement
your_house= FancyHouse()
my_house=FancyHouse(poolhouse=False, lot=10000, basement=True, pool="above-ground")


print(track_house.__str__())
print("___________________")


print(your_house.__str__())
print("___________________")


#Calling the Parent Party method on the Child
#Again, the Class statement took care of the module name
my_house.have_party()

```


<hr>
<br>
</details>
<br>
<br>



#### Setting Managed Properties Inherited from the Parent Take a Little More Work



<br>



If you need to extend the behavior of a _**managed property**_ inherited from a Parent class (extend a setter), extra information needs to be passed (_It's actually an [**open issue**](https://bugs.python.org/issue14965) in the Python language_) :

  **`super(ChildClassName, type(self)).ParentManagedProperty.fset(self, new_value)`**

You can interact with this code snippet [**here**](https://trinket.io/python3/50ff906944)


<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
                     levels=1, bathrooms=2, bedrooms=2,
                     kitchen={'Island':False, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": False, "Bay Windows": False,
                                 "Window Coverings": "Blinds"},
                     diningroom=True, basement=False):

    #"regular" attributes
    self.build_date=build_date
    self.levels=levels
    self.bathrooms=bathrooms
    self.bedrooms=bedrooms
    self.kitchen=kitchen
    self.livingroom=livingroom
    self.diningroom=diningroom
    self.basement=basement
    self.taxes_paid=False

    #managed attributes
    self._property_value=100000.00
    self._markup=.20
    self._tax_rate=.0136

  #getters for managed attributes
  @property
  def property_value(self):
    return self._property_value

  @property
  def list_price(self):
    price = (self._property_value * self._markup + self._property_value)

    return f'${price:,.2f}'

  @property
  def taxes(self):
     return (self._property_value * self._tax_rate)


  #setters for managed attributes
  @property_value.setter
  def property_value(self, value):
    self._property_value = value

  @list_price.setter
  def list_price(self, amount):
    self._property_value=amount / (self._markup + 1)


  #"regular" methods
  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.taxes
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")

  def is_new(self):
    return self.build_date > datetime.date(2010, 11, 15)


  #for printing out a representation of the class.
  def __str__(self):
    return "house specs are:  \n\n" + "\n".join([item[0] + ": " + str(item[1]) for
                                                 item in self.__dict__.items()])


#Here is the child, inheriting from BaseHouse.
class FancyHouse(BaseHouse):

  def __init__(self, build_date=datetime.date(2015, 6, 13),
                     levels=2, bathrooms=3, bedrooms=3,
                     kitchen={'Island':True, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": True, "Bay Windows": True,
                                 "Window Coverings": "Drapes", "Vaulted Ceilings": True},
                     diningroom=True, basement=False, lot=21780,
                     pool="in-ground", poolhouse=True):

    super().__init__(build_date, levels, bathrooms, bedrooms,
                     kitchen, livingroom, diningroom, basement)

    self.pool=pool
    self.poolhouse=poolhouse
    self.lot=lot


  #here we have access to the managed attribute
  #by calling the parent @property through *super()*
  @property
  def property_value(self):
    return super().property_value

  @property
  def list_price(self):
    return super().list_price


  #Here, we have changes to property_value if the lot size is bigger than 15000
  #And so we extend the *setter*. But the call to *super()* needs extra
  #information to work correctly. We need to add the ChildClassName and
  #type(self) as parameters, and call fset(self, value) on the propertyname
  @property_value.setter
  def property_value(self, amount):
    new_amount = (amount + (amount*.02))

    if self.lot > 15000:
      super(FancyHouse,type(self)).property_value.fset(self, new_amount)
    else:
      _property_value = amount
      super(FancyHouse, type(self)).property_value.fset(self, amount)


  #Because we are changing the property_value based on lot size,
  #we have to do it for the list_price setter too.
  @list_price.setter
  def list_price(self, amount):
    adjusted_amount = amount / (self._markup + 1)
    new_amount = (adjusted_amount + (adjusted_amount * .02)) * self._markup

    if self.lot > 1500:
      super(FancyHouse, type(self)).list_price.fset(self, new_amount)

    else:
      _list_price = amount
      super(FancyHouse, type(self)).list_price.fset(self, amount)


  #"regular" methods
  def have_swim_party(self):
    print("We're swimn' and chillin'.  It's a Party!")


  def host_guests(self, guests):
    if self.poolhouse:
      print(', '.join(item for item in guests) + "... staying in the poolhouse." )
    else:
      print(', '.join(item for item in guests) + "... staying in the spare bedroom.")



#Here are some House Objects

#Parent
track_house= BaseHouse()

#Child
your_house= FancyHouse()
my_house=FancyHouse(poolhouse=False)


#The attribute dictionaries for all our objects.
#Parent
print(track_house.__str__())
print("___________________")

#Child
print(your_house.__str__())
print("___________________")

#Child
print(my_house.__str__())
print("___________________")


#Setting the list price on my_house
my_house.list_price=580000


#Setting the property_value on your_house
your_house.property_value=363050

print("___________________")

#Printing Out Attributes again.
print("my_house", my_house.__str__())

print("___________________")

print("your_house", your_house.__str__())
```



<hr>
<br>
</details>
<br>
<br>



#### Child Classes can inherit from more than one Parent.



<br>



List Parents in order of importance. **`ChildClassName(ParentClassName_1, ParentClassName_2)`**

To prevent [**diamond relationships**](https://towardsdatascience.com/how-to-connect-objects-with-each-other-in-different-situations-with-pythonic-ways-d3aaf4c89553), Python resolves property & method names in a specific order (_called the **MRO**_).  The typical MRO is  Child --> (_from left_) Parent_1 --> Parent_2 ....  the first property or method found in the MRO that matches is executed.  We won't go deep in to MRO here, but if you'd like to read more, [**this**](http://sixty-north.com/blog/method-resolution-order-c3-and-super-proxies.html) is a good place to start.

Because of the MRO, if you are extending or overriding inherited methods or properties from Parent_2, you must specify where in the MRO to begin the search by using _**super**_:

**`super(AfterThisClass, self).nameofmethod(args.)`**

This [**series of articles**](http://sixty-north.com/blog/series/pythons-super-explained.html) is an excellent explainer on multiple inheritance and the use of `super()`.

You can interact with this snippet [**here**](https://trinket.io/python3/792d111c02)


<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

#Parent_1
class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
                     levels=1, bathrooms=2, bedrooms=2,
                     kitchen={'Island':False, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": False, "Bay Windows": False,
                                 "Window Coverings": "Blinds"},
                     diningroom=True, basement=False):

    #"regular" attributes
    self.build_date=build_date
    self.levels=levels
    self.bathrooms=bathrooms
    self.bedrooms=bedrooms
    self.kitchen=kitchen
    self.livingroom=livingroom
    self.diningroom=diningroom
    self.basement=basement
    self.taxes_paid=False

    #managed attributes
    self._property_value=100000.00
    self._markup=.20
    self._tax_rate=.0136

  #getters for managed attributes
  @property
  def property_value(self):
    return self._property_value

  @property
  def list_price(self):
    price = (self._property_value * self._markup + self._property_value)

    return f'${price:,.2f}'

  @property
  def taxes(self):
     return (self._property_value * self._tax_rate)


  #setters for managed attributes
  @property_value.setter
  def property_value(self, value):
    self._property_value = value

  @list_price.setter
  def list_price(self, amount):
    self._property_value=amount / (self._markup + 1)


  #"regular" methods
  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.taxes
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")

  def is_new(self):
    return self.build_date > datetime.date(2010, 11, 15)


  #for printing out a representation of the class.
  def __str__(self):
    return "house specs are:  \n\n" + "\n".join([item[0] + ": " + str(item[1]) for
                                                 item in self.__dict__.items()])



#Parent_2
class Condo:
  def __init__(self, build_date=datetime.date(2017, 6, 16),
                     levels=2, bathrooms=2, bedrooms=2,
                     kitchen={"Pantry": True,"oven": True, "Stove": "Gas"}, hoa_dues=300, pmi=150):

      self.build_date=build_date
      self.levels=levels
      self.bathrooms=bathrooms
      self.bedrooms=bedrooms
      self.kitchen=kitchen
      self.hoa_dues=hoa_dues
      self.hoa_dues_paid=False
      self.pmi=pmi

  def pay_hoa_dues(self):
    if self.hoa_dues_paid:
      print("You've already paid the HOA this year.")
    else:
      hoa_amount = self.hoa_dues
      self.hoa_dues_paid = True
      print("You paid " + f'${hoa_amount:,.2f}' + " in HOA dues.")



#Here is the child.
#MRO will be Child -->BaseHouse -->Condo
#Unless otherwise specified by the arguments passed to *super()*
class FancyHouse(BaseHouse, Condo):

  def __init__(self, build_date=datetime.date(2015, 6, 13),
                     levels=2, bathrooms=3, bedrooms=3,
                     kitchen={'Island':True, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": True, "Bay Windows": True,
                                 "Window Coverings": "Drapes", "Vaulted Ceilings": True},
                     diningroom=True, basement=False, hoa_dues=300, pmi=150,
                     lot=21780, pool="in-ground", poolhouse=True):

    #Here, we're calling the __init__ from BaseHouse
    super().__init__(build_date, levels, bathrooms, bedrooms,
                     kitchen, livingroom, diningroom, basement)

    #Here, we're calling the __init__ from Condo.  BaseHouse is passed as the
    #first argument to *super()*. Passing BaseHouse first means that the
    #search for the __init__ method will start *after* BaseHouse
    #-- in the Condo Class, ensuring Condos __init__ is called.
    super(BaseHouse, self).__init__(build_date, levels, bathrooms,
                                    bedrooms, kitchen, hoa_dues, pmi)

    #And, finally, the properties added by this Child Class
    self.pool=pool
    self.poolhouse=poolhouse
    self.lot=lot


  @property
  def property_value(self):
    return super().property_value

  @property
  def list_price(self):
    return super().list_price


  @property_value.setter
  def property_value(self, amount):
    new_amount = (amount + (amount*.02))

    if self.lot > 15000:
      super(FancyHouse,type(self)).property_value.fset(self, new_amount)
    else:
      _property_value = amount
      super(FancyHouse, type(self)).property_value.fset(self, amount)


  @list_price.setter
  def list_price(self, amount):
    adjusted_amount = amount / (self._markup + 1)
    new_amount = (adjusted_amount + (adjusted_amount * .02)) * self._markup

    if self.lot > 1500:
      super(FancyHouse, type(self)).list_price.fset(self, new_amount)

    else:
      _list_price = amount
      super(FancyHouse, type(self)).list_price.fset(self, amount)


  #"regular" methods
  def have_swim_party(self):
    print("We're swimn' and chillin'.  It's a Party!")


  def host_guests(self, guests):
    if self.poolhouse:
      print(', '.join(item for item in guests) + "... staying in the poolhouse." )
    else:
      print(', '.join(item for item in guests) + "... staying in the spare bedroom.")



#Here are some House Objects

#Parent_1
track_house= BaseHouse()

#Parent_2
my_condo=Condo()

#Child
my_house=FancyHouse(poolhouse=False, pmi=0, hoa_dues=450)


#The attribute dictionaries for all our objects.
#Parent
print(track_house.__str__())
print("___________________")

#Condo
print(my_condo.__dict__)
print("___________________")

#Child
print(my_house.__str__())
print("___________________")


#Setting the list price on my_house
#Method inherited (and extended) from BaseHouse
my_house.list_price=580000

print("___________________")

#Paying the taxes on my_house
#Method inherited from BaseHouse
my_house.pay_taxes()


#Paying the HOA dues for my_house.
#Method inherited from Condo
my_house.pay_hoa_dues()

print("___________________")
print("___________________")

#Printing Out Attributes of my_house.
print("my_house", my_house.__str__())

```


<hr>
<br>
</details>
<br>
<br>



#### Composition can be an Alternative to  Inheriting from Multiple Parents


<br>



Rather than go through the complexity of sorting out what to override with multiple inheritance, it may be more straightforward to _**compose**_ a Class with Objects & functionality from other Classes.

 We've actually seen this pattern already -- if you look at the BaseHouse Class, you'll see that one of the properties uses a _**datetime**_ Object.  We don't actually want our BaseHouse to **be** a datetime -- we just want it to _**have**_ a datetime associated with it.  Things having to do with that datetime get forwarded to the datetime Object for processing, but we can take advantage of all it's qualities within our BaseHouse Class anyways.

So what would that mean for our collection of House Classes? Well - a bit of a re-write or clarification.

You can interact with the code snippet [**here**]()



<br>
<details>
<summary>Code Snippet</summary>



```python
import datetime

#Since taxes, pmi, and HOAs are things houes have, we've parked these
#attributes and methods here, and pulled them out of the various house types
class RealEstateFees:
  def __init__(self, **kwargs):
    self.purchase_price=kwargs.get('purchase_price', 100000)
    self.markup=kwargs.get('markup', .20)
    self.current_value=kwargs.get('purchase_price', 0)
    self.tax_rate=kwargs.get('tax_rate', .0136)
    self.hoa_amount=kwargs.get('hoa_amount', 0)
    self.pmi_amount=kwargs.get('pmi_amount' ,0)
    self.tax_amount=0


  def calculate_taxes(self):
      self.tax_amount = (self.purchase_price * self.tax_rate)
      return self.tax_amount


  def calculate_list_price(self):
      price = self.current_value + (self.current_value * self.markup)

      return f'${price:,.2f}'


  def calculate_pmi(self):
    return self.pmi_amount


  def calculate_hoa(self):
    return self.hoa_amount


#Here is the BaseHouse -- now with its own RealEstateFees Object to manage taxes, et. al.
class BaseHouse:
  def __init__(self, build_date=datetime.date(2012, 4, 13),
                     levels=1, bathrooms=2, bedrooms=2,
                     kitchen={'Island':False, "Pantry": True,
                              "oven": True, "Stove": "Gas"},
                     livingroom={"Fireplace": True, "Bay Windows": True,
                                 "Window Coverings": "Drapes", "Vaulted Ceilings": True},
                     diningroom=True, basement=False,
                     stats={'hoa_amount':300, 'pmi_amount':150,
                            'tax_rate':.0136, 'markup':.20,
                            'purchase_price': 200000}):

    self.build_date=build_date
    self.levels=levels
    self.bathrooms=bathrooms
    self.bedrooms=bedrooms
    self.kitchen=kitchen
    self.livingroom=livingroom
    self.diningroom=diningroom
    self.basement=basement
    self.taxes_paid=False
    self.hoa_paid=False
    self.pmi_paid=False


    #Here we are using a RealEstateFees Object to Manage the fees & property values
    self.real_estate_details=RealEstateFees(**stats)


 #Managed attributes
  @property
  def property_value(self):
      return self.real_estate_details.current_value


  @property
  def list_price(self):
    return self.real_estate_details.calculate_list_price()


  #setters for managed attributes
  @property_value.setter
  def property_value(self, value):
    self.real_estate_details.current_value=value

  @list_price.setter
  def list_price(self, amount):
    self.real_estate_details.current_value = amount /(self.real_estate_details.markup + 1)


  def is_new(self):
    return self.build_date > datetime.date(2010, 11, 15)

  #I still pay taxes, but I don't *calculate* them -- the RealEstateFees does that for me
  def pay_taxes(self):
    if self.taxes_paid:
      print("You've already paid property taxes this year.")
    else:
      tax_amount = self.real_estate_details.calculate_taxes()
      self.taxes_paid = True
      print("You paid " + f'${tax_amount:,.2f}' + " in property taxes.")

  #same with HOA fees
  def pay_hoa(self):
    if self.hoa_paid:
      print("You've already paid the HOA this month.")
    else:
      hoa_amount = self.real_estate_details.calculate_hoa()
      self.hoa_paid = True
      print("You paid " + f'${hoa_amount:,.2f}' + " in HOA dues this month.")


  #for printing out a representation of the class.
  #note the second unpack, because RealEstateFees doesn't have it's own __str__
  def __str__(self):
    property_details = "\n".join([item[0] + ": "
                        + str(item[1]) for item in
                              self.real_estate_details.__dict__.items()])

    house_specs = "\n".join([item[0] + ": "
                  + str(item[1]) for item in
                        self.__dict__.items() if item[0] != 'real_estate_details'])

    specs= "house specs are:  " + "\n\n" + house_specs + "\n\n" + property_details

    return specs



#Here are some House Objects

#Parent_1
our_house= BaseHouse()


#The attribute dictionaries for all our objects.
#Parent
print(our_house.__str__())
print("___________________")


#Setting the list price on my_house
#The setter delegates to setting RealEstateFees.current_value
our_house.list_price=580000

#printing the new property_value based on list price
print("Property Value: ", our_house.property_value)

##double-checking list price
print("List Price: ", our_house.list_price)

print("___________________")

#Paying the taxes on my_house
our_house.pay_taxes()


#Paying the HOA dues for my_house.
our_house.pay_hoa()

#Calling pay_hoa() a second time
our_house.pay_hoa()

print("___________________")
print("___________________")

#Printing Out Attributes of my_house.
print("our_house", our_house.__str__())


```



<hr>
<br>
</details>
<br>
<br>



There's _energetic debate_ about Composition vs Inheritance, which we aren't going to discuss at length.  Both have benefits & drawbacks, & those change radically depending on your particular data model & use case.  [**this**](https://en.wikipedia.org/wiki/Composition_over_inheritance) & [**this**](http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-3-delegation-composition-and-inheritance/) are two places to read more about Composition as a design principal in OOP.


<br>
<br>



#### Mixin Classes are Another Way to Borrow Functionality


<br>



A _**Mixin**_ is a variant on multiple inheritance that edges it closer to composition-like behavior.  A _**Mixin**_ Class is usually designed with generic functionality that's there _soley for the purpose of inheriting it into other classes_.  Mixins aren not intended to stand on their own as a Parent Class -- they're code that's shared by a number of _other_ Classes that already have their own "main" Parent or base Class.

**_`RealEstateFees`_** above  could be used as a Mixin, although you might want to refactor even it a bit more.  For a good example of how one Django developer uses this pattern, read  [**here**](https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556).  For additional explanations and examples read [**here**](https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful) & [**here**](https://andrewbrookins.com/technology/mixins-in-python-and-ruby-compared/#what-is-a-mixin).



<br>
<br>



### Next Steps


<br>



Depending on your background that was a lot of review -- or a lot to think about.  To help the process, we've given you a small [**OOP homework exercise**](./homework/README.md), adapted from [**exercism.io**](exercism.io).  If you'd like even more OOP exercises, the homework page has some suggested exercism.io and other problems to tackle.
