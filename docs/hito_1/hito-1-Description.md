# PoDeMaster -- Cloud Computing Project 
*Hito 1 -- Cloud Computing Project by Omid Rajabi*
![PoDeMaster Logo](../images/PoDeMaster-Logo.png)

### Project Description
*Problem:* 
Pokémon is the largest multimedia franchise in the world, with a vast and dedicated global community. A significant part of this community consists of Pokémon players (PP), who contribute to its enduring success. Currently, there are a total of 38 mainline Pokémon games, featuring over 1,000 unique Pokémon species. The primary goal in these games is to "catch 'em all"—collecting every available Pokémon to complete the Pokédex. To assist with this, the Pokémon Company (PC) has developed the App Pokemon Home, which allows players to store and organize the Pokémon they've caught across different games. However, within the community, there's an even more ambitious goal known as the "Living Dex." This challenge requires players to not only catch every Pokémon but to have a living exemplar of each species physically stored in the app. Unfortunately, the current PC app does not fully support this "Living Dex" challenge, as it lacks features tailored to managing and showcasing one of each Pokémon species in real-time. It is also not possible to check which game allows you to obtain which Pokémon or even to organize the Pokémon you have already collected by their number. This gap has created demand among collectors for a more comprehensive solution that caters to this specific goal.

*Solving:*
We propose the creation of a cloud-based solution that allows Pokémon players to digitally "create" and store the Pokémon they own. This system would let users input key details about their Pokémon, such as the game they were caught in, original trainer (OT), alternate forms, shiny status, and potentially even stats, storing this data on a central server.
With this system, users could easily track their progress in completing their Pokédex, seeing which Pokémon they have and which are still missing. The platform would display which generations the player has fully completed and provide a clear breakdown of missing species. For each missing Pokémon, the system would offer information on where to find or obtain it, including the specific games or methods.
As an additional feature, the platform could help users find potential trade partners to obtain their missing Pokémon, fostering greater community engagement and facilitating the completion of their collections.

*Who benefits?*
- Casual Players who only want to complete their collection
- Collectors who are looking for a specific Pokémon and want to have a visual way to manage their collection
- Players who want to trade

*Why Cloud Based?* 
- Cloud handles all the logic for storing Pokémon details, tracking user progress, and generating real-time reports of missing Pokémon.
- Players can access their data from any device since it is stored on the cloud, ensuring convenience and allowing Multi-User Collaboration.
- A cloud-based solution allows users to access their Dex across multiple platforms (mobile, web, etc.).

*Core Features:*
- User registration and login.
- Input form to add Pokémon details (basic CRUD functionality).
- Living Dex progress display (missing/collected Pokémon with simple statistics).
- Missing Pokémon info (from a static dataset of Pokémon availability across games).

*Optional Features (if time permits):*
- Search for specific Pokémon in the Living Dex.
- Trade partner matching.
- Notifications for new trade offers.

*Technology – What do we need?* 
- Frontend: Simple web interface (React?)
- Backend: Server-side logic using something like Node.js or Python to manage Pokémon Data
- Database: Cloud-based database to store users and Pokémon details 

