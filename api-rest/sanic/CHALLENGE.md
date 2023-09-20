# Challenge
## Part 1
1. Create a infrastructure layer responsible to manage mongodb connection and provide database access;
2. Use the provided database to create repository layer to create a petshop repository that uses 'petshop' colletion;
3. Create pet repository that uses 'pet' collection;
4. Create endpoints to create, update, find_all, find_one and delete_one documents of 'petshop' collection;
5. Create endpoints to create, update, find_all, find_one and delete_one documents of 'pet';

# Part 2
1. Create a PetshopModel to validate the user input and add as functionality on POST method;
2. Use the PetshopModel to format the return of POST method;
3. Use the PetshopModel to format the return of GET method on get_one;
4. Use the ListPetshop to format the return of GET method on get_all;
5. Use the UpdatePetshopModel to validate the user input and add as functionality on PATCH method;
6. Use the PetshopModel to format the return of PATCH method on update_one;
7. Use the PetModel to validate the user input and add as functionality on POST method;
8. Use the PetModel to format the return of POST method;
9. Use the PetModel to format the return of GET method on get_one;
10. Use the ListPet to format the return of GET method on get_all;
11. Use the UpdatePetModel to validate the user input and add as functionality on PATCH method;
12. Use the PetModel to format the return of PATCH method on update_one

# Part 3
1. Create an auto reconnection to database, test it with 'docker compose down' and 'docker compose up -d mongo' commands, do requests when database is down and repeat when database is up;
2. Identify database disconnection status and log it;