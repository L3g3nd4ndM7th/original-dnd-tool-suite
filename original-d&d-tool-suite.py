import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, Toplevel
import random
from random import randint

def main():
    root = tk.Tk()
    root.title("Custom Tkinter App")
    root.geometry('750x500')
    
    adventures = {
        "All": None
        }
    
    characters = {
        "Character 1": {},
        "Character 2": {},
        "Character 3": {},
        "Character 4": {},
        "Character 5": {},
        "Character 6": {},
        "Character 7": {},
        "Character 8": {},
        "Character 9": {},
        "Character 10": {},
        "Character 11": {},
        "Character 12": {},
        "Character 13": {},
        "Character 14": {},
        "Character 15": {},
        "Character 16": {},
        "Character 17": {},
        "Character 18": {},
        "Character 19": {},
        "Character 20": {},
    }

    monsters = ['Goblin', 'Bandit', 'Skeleton', 'Giant Rat', 'Giant Bat']
    
    def roll_dice(dice):
        dice_multiplier = int(entry_dice_multiplier.get())
        dice_rolls = int(entry_dice_rolls.get())

        all_rolls = []
        all_sums = []

        for roll_index in range(dice_rolls):
            rolls = []
            dice_sum = 0

            for i in range(dice_multiplier):
                roll = randint(1, dice)
                rolls.append(roll)
                dice_sum += roll

            all_rolls.append(rolls)
            all_sums.append(dice_sum)

        text_dice_log.config(state=tk.NORMAL)
        text_dice_log.insert(tk.END, '\n')
        text_dice_log.insert(tk.END, f'Rolled {dice_rolls} {dice_multiplier}d{dice}:\n')
        for rolls, dice_sum in zip(all_rolls, all_sums):
            text_dice_log.insert(tk.END, ', '.join(map(str, rolls)))
            if dice_multiplier > 1:
                text_dice_log.insert(tk.END, f' = {dice_sum}\n')
            else:
                text_dice_log.insert(tk.END, '\n')

        text_dice_log.delete("end-2c", "end-1c")
        text_dice_log.config(state=tk.DISABLED)
        text_dice_log.yview_moveto(1.0)

    def create_new_adventure():
        new_adventure_name = simpledialog.askstring("Create New Adventure", "Enter a name for the new adventure:")
        
        if new_adventure_name is not None:  # Check if the user didn't close the dialog
            if new_adventure_name:
                if new_adventure_name in adventures:
                    messagebox.showinfo("Adventure Exists", f"An adventure named '{new_adventure_name}' already exists.")
                else:
                    adventures[new_adventure_name] = []
                    combobox_adventures["values"] = list(adventures.keys())
                    combobox_adventures.set(new_adventure_name)
                    combobox_characters["values"] = []
                    combobox_characters.set("Select Character")
                    combobox_adventures.set(new_adventure_name)
            else:
                messagebox.showinfo("Empty Name Field", "Please enter a name for the new adventure.")
                create_new_adventure()

    def delete_adventure():
        selected_adventure = combobox_adventures.get()

        if selected_adventure == "All":
            messagebox.showinfo("Cannot Delete All", "You cannot delete the default 'All' adventure.")
            return

        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the '{selected_adventure}' adventure?")

        if confirm:
            if selected_adventure in adventures:
                del adventures[selected_adventure]
                combobox_adventures["values"] = list(adventures.keys())
                combobox_adventures.set("All")
                combobox_characters["values"] = list(characters.keys())
                combobox_characters.set(combobox_characters["values"][0] if combobox_characters["values"] else "Select Character")

    def rename_adventure():
        selected_adventure = combobox_adventures.get()
        if selected_adventure == "All":
            messagebox.showinfo("Cannot Rename All", "You cannot delete the default 'All' adventure.")
            return
        
        new_adventure_name = simpledialog.askstring("Rename Adventure", f"Enter new name for '{selected_adventure}':")

        if new_adventure_name and selected_adventure in adventures:
            adventures[new_adventure_name] = adventures[selected_adventure]
            del adventures[selected_adventure]
            combobox_adventures["values"] = list(adventures.keys())
            combobox_adventures.set(new_adventure_name)
            
    def load_adventure(event):
        selected_adventure = combobox_adventures.get()
        updated_adventures = list(adventures.keys())

        combobox_adventures["values"] = updated_adventures
        combobox_adventures.set(selected_adventure if selected_adventure in updated_adventures else updated_adventures[-1])

        if selected_adventure == "All":
            combobox_characters["values"] = list(characters.keys())
            combobox_characters.set(combobox_characters["values"][0])  # Set to the first character
        elif selected_adventure in adventures:
            character_keys = adventures[selected_adventure]
            combobox_characters["values"] = character_keys

            if character_keys:
                combobox_characters.set(character_keys[0])
            else:
                combobox_characters["values"] = []
                combobox_characters.set("Select Character")
        else:
            combobox_characters["values"] = []
            combobox_characters.set("Select Character")
            
        load_character(event)

    def add_monster():
        selected_monster_type = combobox_monster_type.get()
        if selected_monster_type in combobox_monster_type["values"]:
            create_monster_frame(selected_monster_type)

    def add_custom_monster():
        custom_monster_name = simpledialog.askstring("Custom Monster", "Enter custom monster name:")
        if custom_monster_name:
            create_monster_frame(custom_monster_name)

    def create_monster_frame(monster):
        monster_frame = tk.Frame(scrollable_frame, borderwidth=1, relief='groove')
        monster_frame.pack(expand=True, fill='x')

        monster_id = len(scrollable_frame.winfo_children())

        label1 = tk.Label(monster_frame, text=monster_id)
        label1.pack(side='left', padx=2)

        label2 = tk.Label(monster_frame, text=monster)
        label2.pack(side='left', padx=2)
        entry3 = tk.Entry(monster_frame)
        entry3.pack(side='left', expand=True, fill='x')
        entry3.insert(0, 'HP / AC / Note')
        
        monster_id_values = list(combobox_monster_id['values'])
        monster_id_values.append(len(scrollable_frame.winfo_children()))
        combobox_monster_id['values'] = monster_id_values
        combobox_monster_id.set(monster_id)
        root.update_idletasks()
        scrollable_canvas.yview_moveto(1.0)

    def remove_monster():
        selected_id = combobox_monster_id.get()

        # Find and remove the selected monster frame
        for frame in scrollable_frame.winfo_children():
            frame_id = str(frame.winfo_children()[0].cget("text"))
            if frame_id == selected_id:
                frame.destroy()
                break
        
        frame_count = len(scrollable_frame.winfo_children())
        combobox_monster_id["values"] = list(range(1, frame_count + 1))
        if not combobox_monster_id['values']:
            combobox_monster_id.set('Select ID')
        else:
            combobox_monster_id.set(len(combobox_monster_id["values"]))

        # Re-order frame indexing
        for i, frame in enumerate(scrollable_frame.winfo_children()):
            label = frame.winfo_children()[0]
            label.config(text=str(i + 1))

    def create_new_character():
        selected_adventure = combobox_adventures.get()
        if selected_adventure in adventures:
            new_character_name = "New Character 1"
            index = 1
            while new_character_name in characters:
                index += 1
                new_character_name = f"New Character {index}"
            
            new_character = {
                "Name": "",
                "Race": "",
                "Class": "",
                "Alignment": "",
                "Level": "",
                "Experience": "",
                "HP": "",
                "AC": "",
                "Strength": "",
                "Intelligence": "",
                "Wisdom": "",
                "Dexterity": "",
                "Constitution": "",
                "Charisma": "",
                "Skills": "",
                "Inventory": "",
                "Notes": ""
            }
            
            if selected_adventure != "All":
                adventures[selected_adventure].append(new_character_name)
            
            characters[new_character_name] = new_character

            if selected_adventure != "All":
                combobox_characters["values"] = adventures[selected_adventure]
            else:
                combobox_characters["values"] = list(characters.keys())
                
            entry_name.delete(0, tk.END)
            entry_race.delete(0, tk.END)
            entry_class.delete(0, tk.END)
            entry_alignment.delete(0, tk.END)
            entry_level.delete(0, tk.END)
            entry_experience.delete(0, tk.END)
            entry_hit_points.delete(0, tk.END)
            entry_armor_class.delete(0, tk.END)
            entry_strength.delete(0, tk.END)
            entry_intelligence.delete(0, tk.END)
            entry_wisdom.delete(0, tk.END)
            entry_dexterity.delete(0, tk.END)
            entry_constitution.delete(0, tk.END)
            entry_charisma.delete(0, tk.END)
            text_skills.delete("1.0", tk.END)
            text_inventory.delete("1.0", tk.END)
            text_notes.delete("1.0", tk.END)
                
            combobox_characters.set(new_character_name)
            messagebox.showinfo("New Character Created", "New character created.")
        else:
            messagebox.showinfo("No Adventure Selected", "Please select an adventure before creating a character.")

    def delete_character():
        selected_adventure = combobox_adventures.get()
        selected_character = combobox_characters.get()

        if not selected_character in characters:
            return

        if selected_adventure == "All":
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{selected_character}'?")

            if confirm:
                del characters[selected_character]
                for adventure in adventures:
                    if adventure != "All" and selected_character in adventures[adventure]:
                        adventures[adventure].remove(selected_character)
                combobox_characters["values"] = list(characters.keys())
                combobox_characters.set(combobox_characters["values"][0] if combobox_characters["values"] else "Select Character")
                messagebox.showinfo("Character Deleted", "Character deleted.")
                load_character(event=None)
        else:
            confirm = messagebox.askyesno("Confirm Removal", f"Remove '{selected_character}' from '{selected_adventure}'?")

            if confirm:
                adventures[selected_adventure].remove(selected_character)
                combobox_characters["values"] = adventures[selected_adventure]
                combobox_characters.set(combobox_characters["values"][0] if combobox_characters["values"] else "Select Character")
                messagebox.showinfo("Character Removed", f"Character '{selected_character}' removed from '{selected_adventure}'.")
                load_character(event=None)
            
    def load_character(event):
        selected_character = combobox_characters.get()
        
        if selected_character in characters:
            character_data = characters[selected_character]
            
            entry_name.delete(0, tk.END)
            entry_name.insert(0, character_data.get("Name", ""))
            
            entry_race.delete(0, tk.END)
            entry_race.insert(0, character_data.get("Race", ""))
            
            entry_class.delete(0, tk.END)
            entry_class.insert(0, character_data.get("Class", ""))
            
            entry_alignment.delete(0, tk.END)
            entry_alignment.insert(0, character_data.get("Alignment", ""))
            
            entry_level.delete(0, tk.END)
            entry_level.insert(0, character_data.get("Level", ""))
            
            entry_experience.delete(0, tk.END)
            entry_experience.insert(0, character_data.get("Experience", ""))
            
            entry_hit_points.delete(0, tk.END)
            entry_hit_points.insert(0, character_data.get("HP", ""))
            
            entry_armor_class.delete(0, tk.END)
            entry_armor_class.insert(0, character_data.get("AC", ""))
            
            entry_strength.delete(0, tk.END)
            entry_strength.insert(0, character_data.get("Strength", ""))
            
            entry_intelligence.delete(0, tk.END)
            entry_intelligence.insert(0, character_data.get("Intelligence", ""))
            
            entry_wisdom.delete(0, tk.END)
            entry_wisdom.insert(0, character_data.get("Wisdom", ""))
            
            entry_dexterity.delete(0, tk.END)
            entry_dexterity.insert(0, character_data.get("Dexterity", ""))
            
            entry_constitution.delete(0, tk.END)
            entry_constitution.insert(0, character_data.get("Constitution", ""))
            
            entry_charisma.delete(0, tk.END)
            entry_charisma.insert(0, character_data.get("Charisma", ""))
            
            text_skills.delete("1.0", tk.END)
            text_skills.insert("1.0", character_data.get("Skills", ""))
            
            text_inventory.delete("1.0", tk.END)
            text_inventory.insert("1.0", character_data.get("Inventory", ""))
            
            text_notes.delete("1.0", tk.END)
            text_notes.insert("1.0", character_data.get("Notes", ""))
                
    def add_hour():
        current_hour = int(entry_hour.get())
        entry_hour.delete(0, tk.END)
        entry_hour.insert(0, str(current_hour + 1))

    def add_day():
        current_day = int(entry_day.get())
        entry_day.delete(0, tk.END)
        entry_day.insert(0, str(current_day + 1))

    def on_key_return_entry(event):
        widget = event.widget
        property_name = widget.property_name

        selected_character = combobox_characters.get()

        if selected_character in characters:
            characters_data = characters[selected_character]
            characters_data[property_name] = widget.get()
            characters[selected_character] = characters_data
            print(characters[selected_character])

    def on_key_return_text(event):
        widget = event.widget
        property_name = widget.property_name

        selected_character = combobox_characters.get()

        if selected_character in characters:
            characters_data = characters[selected_character]
            characters_data[property_name] = widget.get("1.0", "end-1c")
            characters[selected_character] = characters_data
            print(characters[selected_character])

    def open_character_loader():
        def load_character_to_adventure():
            selected_adventure = combobox_adventures.get()
            
            selected_characters = listbox_character_loader.curselection()
            
            if selected_characters:
                selected_characters = [listbox_character_loader.get(index) for index in selected_characters]
                adventures[selected_adventure].extend(selected_characters)
                
                combobox_adventures.set(selected_adventure)
                combobox_characters["values"] = adventures[selected_adventure]
                combobox_characters.set(combobox_characters["values"][0] if combobox_characters["values"] else "Select Character")
                load_character(event=None)
                
                messagebox.showinfo("Characters Loaded", f"Characters successfully loaded into {selected_adventure}.")
                
        selected_adventure = combobox_adventures.get()
        
        if selected_adventure == "All":
            messagebox.showinfo("Cannot Load into All", "You cannot load characters into the default 'All' adventure.")
            return
        
        toplevel_character_loader = Toplevel(root)

        label_select_character_to_load= tk.Label(toplevel_character_loader, text="Select character(s) to load")
        label_select_character_to_load.pack()
    
        frame_character_loader = tk.Frame(toplevel_character_loader)
        frame_character_loader.pack()
        
        listbox_character_loader = tk.Listbox(frame_character_loader, selectmode=tk.MULTIPLE)
        listbox_character_loader.pack(side='left')

        button_load_character = tk.Button(toplevel_character_loader, text="Load", command=load_character_to_adventure)
        button_load_character.pack()

        scrollbar_listbox_character_loader = ttk.Scrollbar(frame_character_loader)
        scrollbar_listbox_character_loader.pack(side='right', fill='y')
        scrollbar_listbox_character_loader.config(command=listbox_character_loader.yview)
        listbox_character_loader.config(yscrollcommand=scrollbar_listbox_character_loader.set)

        for character in characters:
            listbox_character_loader.insert(tk.END, character)

    def random_biome():
        biomes = ["jjfdosajf joijoijsfd pifsdopjfasdfojdfp odsjfpaifdf pdjsadfjopjf jfdpisfpadpf osdafodsafp dsfiajpdf dsaopjfo"]
        result = random.choice(biomes)
        label_random_encounter.config(text=result)

    def random_terrain():
        terrains = ["Plains", "Cave", "Canyon", "Jungle", "Tundra"]
        result = random.choice(terrains)
        label_random_encounter.config(text=result)

    def random_weather():
        weather = ["Clear", "Rainy", "Snowy", "Foggy", "Stormy"]
        result = random.choice(weather)
        label_random_encounter.config(text=result)

    def random_event():
        events = ["Encounter with a traveler", "Discovery of a hidden cave", "Unusual celestial event", "Mysterious illness spreads"]
        result = random.choice(events)
        label_random_encounter.config(text=result)

    def random_npc():
        npcs = ["Friendly merchant", "Mysterious sorcerer", "Grumpy tavern keeper", "Eccentric bard", "Shady rogue"]
        result = random.choice(npcs)
        label_random_encounter.config(text=result)

    def random_treasure():
        treasures = ["Ancient artifact", "Bag of gold coins", "Magic potion", "Enchanted weapon", "Jeweled crown"]
        result = random.choice(treasures)
        label_random_encounter.config(text=result)

    def random_trap():
        traps = ["Hidden pitfall", "Poisoned dart trap", "Blade-swinging pendulum", "Pressure plate activating spikes", "Illusory floor"]
        result = random.choice(traps)
        label_random_encounter.config(text=result)

    frame_module_selection = tk.Frame(root)
    frame_module_selection.pack()

    ####################
    ####################
    ####################
    ####################
    ####################

    frame_module_dice_roller = tk.Frame(root)
    frame_module_dice_roller.pack(anchor='center', expand=True)

    frame_dice_roller_controls = tk.Frame(frame_module_dice_roller)
    frame_dice_roller_controls.pack()

    label_dice_rolls = tk.Label(frame_dice_roller_controls, text="Rolls")
    label_dice_rolls.pack(side='left')

    entry_dice_rolls = tk.Entry(frame_dice_roller_controls, width=5)
    entry_dice_rolls.pack(side="left")
    entry_dice_rolls.insert(0, 1)

    label_dice_amount = tk.Label(frame_dice_roller_controls, text="Dice")
    label_dice_amount.pack(side="left")

    entry_dice_multiplier = tk.Entry(frame_dice_roller_controls, width=5)
    entry_dice_multiplier.pack(side="left")
    entry_dice_multiplier.insert(0, 1)

    frame_dice_buttons = tk.Frame(frame_module_dice_roller)
    frame_dice_buttons.pack()

    button_roll_d4 = tk.Button(frame_dice_buttons, text="d4", command=lambda: roll_dice(4))
    button_roll_d4.pack(side="left")

    button_roll_d6 = tk.Button(frame_dice_buttons, text="d6", command=lambda: roll_dice(6))
    button_roll_d6.pack(side="left")

    button_roll_d8 = tk.Button(frame_dice_buttons, text="d8", command=lambda: roll_dice(8))
    button_roll_d8.pack(side="left")

    button_roll_d10 = tk.Button(frame_dice_buttons, text="d10", command=lambda: roll_dice(10))
    button_roll_d10.pack(side="left")

    button_roll_d12 = tk.Button(frame_dice_buttons, text="d12", command=lambda: roll_dice(12))
    button_roll_d12.pack(side="left")

    button_roll_d20 = tk.Button(frame_dice_buttons, text="d20", command=lambda: roll_dice(20))
    button_roll_d20.pack(side="left")

    button_roll_d100 = tk.Button(frame_dice_buttons, text="d100", command=lambda: roll_dice(100))
    button_roll_d100.pack(side="left")

    frame_dice_log = tk.Frame(frame_module_dice_roller)
    frame_dice_log.pack()

    text_dice_log = tk.Text(frame_dice_log, width=40, height=10, wrap="word", state="disabled")
    text_dice_log.pack()

    ####################
    ####################
    ####################
    ####################
    ####################

    frame_module_character_manager = tk.Frame(root,)

    frame_adventure_controls = tk.Frame(frame_module_character_manager)
    frame_adventure_controls.pack()

    label_adventure = tk.Label(frame_adventure_controls, text="Adventures")
    label_adventure.pack(side="left")

    combobox_adventures = ttk.Combobox(frame_adventure_controls, values=list(adventures.keys()), state="readonly")
    combobox_adventures.pack(side="left")
    combobox_adventures.set(combobox_adventures['values'][0])
    combobox_adventures.bind("<<ComboboxSelected>>", load_adventure)

    button_new_adventure = tk.Button(frame_adventure_controls, text="New", command=create_new_adventure)
    button_new_adventure.pack(side="left")

    button_delete_adventure = tk.Button(frame_adventure_controls, text="Delete", command=delete_adventure)
    button_delete_adventure.pack(side="left")

    button_rename_adventure = tk.Button(frame_adventure_controls, text="Rename", command=rename_adventure)
    button_rename_adventure.pack(side="left")

    frame_character_controls = tk.Frame(frame_module_character_manager)
    frame_character_controls.pack()

    label_character = tk.Label(frame_character_controls, text="Characters")
    label_character.pack(side="left")

    combobox_characters = ttk.Combobox(frame_character_controls, values=list(characters.keys()), state="readonly")
    combobox_characters.pack(side="left")
    combobox_characters.set(combobox_characters['values'][0])
    combobox_characters.bind("<<ComboboxSelected>>", load_character)

    button_new_character = tk.Button(frame_character_controls, text="New", command=create_new_character)
    button_new_character.pack(side="left")

    button_delete_character = tk.Button(frame_character_controls, text="Delete", command=delete_character)
    button_delete_character.pack(side="left")

    button_load_character = tk.Button(frame_character_controls, text="Load", command=open_character_loader)
    button_load_character.pack()

    frame_character_info = tk.Frame(frame_module_character_manager)
    frame_character_info.pack()

    label_name = tk.Label(frame_character_info, text="Name", width=10)
    label_name.pack(side="left")

    entry_name = tk.Entry(frame_character_info)
    entry_name.pack(side="left")

    label_race = tk.Label(frame_character_info, text="Race", width=10)
    label_race.pack(side="left")

    entry_race = tk.Entry(frame_character_info)
    entry_race.pack(side="left")

    frame_character_class = tk.Frame(frame_module_character_manager)
    frame_character_class.pack()

    label_class = tk.Label(frame_character_class, text="Class", width=10)
    label_class.pack(side="left")

    entry_class = tk.Entry(frame_character_class)
    entry_class.pack(side="left")

    label_alignment = tk.Label(frame_character_class, text="Alignment", width=10)
    label_alignment.pack(side="left")

    entry_alignment = tk.Entry(frame_character_class)
    entry_alignment.pack(side="left")

    frame_character_level = tk.Frame(frame_module_character_manager)
    frame_character_level.pack()

    label_level = tk.Label(frame_character_level, text="Level", width=5)
    label_level.pack(side="left")

    entry_level = tk.Entry(frame_character_level, width=5)
    entry_level.pack(side="left")

    label_experience = tk.Label(frame_character_level, text="Experience", width=10)
    label_experience.pack(side="left")

    entry_experience = tk.Entry(frame_character_level, width=15)
    entry_experience.pack(side="left")

    label_hit_points = tk.Label(frame_character_level, text="HP", width=3)
    label_hit_points.pack(side="left")

    entry_hit_points = tk.Entry(frame_character_level, width=5)
    entry_hit_points.pack(side="left")

    label_armor_class = tk.Label(frame_character_level, text="AC", width=3)
    label_armor_class.pack(side="left")

    entry_armor_class = tk.Entry(frame_character_level, width=5)
    entry_armor_class.pack(side="left")

    frame_character_stats = tk.Frame(frame_module_character_manager)
    frame_character_stats.pack()

    label_strength = tk.Label(frame_character_stats, text="Strength", width=10)
    label_strength.pack(side="left")

    entry_strength = tk.Entry(frame_character_stats, width=5)
    entry_strength.pack(side="left")

    label_intelligence = tk.Label(frame_character_stats, text="Intelligence", width=10)
    label_intelligence.pack(side="left")

    entry_intelligence = tk.Entry(frame_character_stats, width=5)
    entry_intelligence.pack(side="left")

    label_wisdom = tk.Label(frame_character_stats, text="Wisdom", width=10)
    label_wisdom.pack(side="left")

    entry_wisdom = tk.Entry(frame_character_stats, width=5)
    entry_wisdom.pack(side="left")

    frame_character_attributes = tk.Frame(frame_module_character_manager)
    frame_character_attributes.pack()

    label_dexterity = tk.Label(frame_character_attributes, text="Dexterity", width=10)
    label_dexterity.pack(side="left")

    entry_dexterity = tk.Entry(frame_character_attributes, width=5)
    entry_dexterity.pack(side="left")

    label_constitution = tk.Label(frame_character_attributes, text="Constitution", width=10)
    label_constitution.pack(side="left")

    entry_constitution = tk.Entry(frame_character_attributes, width=5)
    entry_constitution.pack(side="left")

    label_charisma = tk.Label(frame_character_attributes, text="Charisma", width=10)
    label_charisma.pack(side="left")

    entry_charisma = tk.Entry(frame_character_attributes, width=5)
    entry_charisma.pack(side="left")

    frame_character_skills = tk.Frame(frame_module_character_manager)
    frame_character_skills.pack()

    label_skills = tk.Label(frame_character_skills, text="Skills", width=10)
    label_skills.pack(side="left")

    text_skills = tk.Text(frame_character_skills, width=40, height=4)
    text_skills.pack(side="left")

    frame_character_inventory = tk.Frame(frame_module_character_manager)
    frame_character_inventory.pack()

    label_inventory = tk.Label(frame_character_inventory, text="Inventory", width=10)
    label_inventory.pack(side="left")

    text_inventory = tk.Text(frame_character_inventory, width=40, height=4)
    text_inventory.pack(side="left")

    frame_character_notes = tk.Frame(frame_module_character_manager)
    frame_character_notes.pack()

    label_notes = tk.Label(frame_character_notes, text="Notes", width=10)
    label_notes.pack(side="left")

    text_notes = tk.Text(frame_character_notes, width=40, height=4)
    text_notes.pack(side="left")

    ####################
    ####################
    ####################
    ####################
    ####################

    frame_module_adventure_log = tk.Frame(root)

    frame_adventure_controls_log = tk.Frame(frame_module_adventure_log)
    frame_adventure_controls_log.pack()

    combobox_adventure_log = ttk.Combobox(frame_module_adventure_log, state="readonly")
    combobox_adventure_log.pack()
    combobox_adventure_log.set("Select Adventure")

    frame_adventure_log_controls2 = tk.Frame(frame_module_adventure_log)
    frame_adventure_log_controls2.pack()

    label_day = tk.Label(frame_adventure_log_controls2, text="Day:")
    label_day.pack(side='left')

    entry_day = tk.Entry(frame_adventure_log_controls2, width=5)
    entry_day.pack(side='left')
    entry_day.insert(0, 1)

    button_add_day = tk.Button(frame_adventure_log_controls2, text='+', command=add_day)
    button_add_day.pack(side='left')

    label_hour = tk.Label(frame_adventure_log_controls2, text="Hour:")
    label_hour.pack(side='left')

    entry_hour = tk.Entry(frame_adventure_log_controls2, text="1", width=5)
    entry_hour.pack(side='left')
    entry_hour.insert(0, 1)

    button_add_hour = tk.Button(frame_adventure_log_controls2, text='+', command=add_hour)
    button_add_hour.pack(side='left')

    frame_log_text = tk.Frame(frame_module_adventure_log)
    frame_log_text.pack()

    label_log = tk.Label(frame_log_text, text="Log")
    label_log.pack(side='left')

    text_log = tk.Text(frame_log_text, width=60, height=12)
    text_log.pack(side='left')

    ####################
    ####################
    ####################
    ####################
    ####################

    frame_module_monster_spawner = tk.Frame(root)

    frame_monster_controls = tk.Frame(frame_module_monster_spawner)
    frame_monster_controls.pack()

    label_monster_type = tk.Label(frame_monster_controls, text="Monster type")
    label_monster_type.pack(side="left")

    combobox_monster_type = ttk.Combobox(frame_monster_controls, values=monsters, state="readonly")
    combobox_monster_type.pack(side="left")
    combobox_monster_type.set("Select Monster")

    button_add_monster = tk.Button(frame_monster_controls, text="Add", command=add_monster)
    button_add_monster.pack(side="left")

    button_add_monster_custom = tk.Button(frame_monster_controls, text="Add Custom", command=add_custom_monster)
    button_add_monster_custom.pack(side="left")

    frame_monster_id_controls = tk.Frame(frame_module_monster_spawner)
    frame_monster_id_controls.pack()

    label_monster_id = tk.Label(frame_monster_id_controls, text="Monster ID")
    label_monster_id.pack(side="left")

    combobox_monster_id = ttk.Combobox(frame_monster_id_controls, state="readonly")
    combobox_monster_id.pack(side="left")
    combobox_monster_id.set("Select ID")

    button_delete_monster = tk.Button(frame_monster_id_controls, text="Remove", command=remove_monster)
    button_delete_monster.pack(side="left")

    frame_monster_list = tk.Frame(frame_module_monster_spawner) 
    frame_monster_list.pack()

    scroller = ttk.Scrollbar(frame_monster_list, orient='vertical')
    scroller.pack(side='right', fill='y')

    scrollable_canvas = tk.Canvas(frame_monster_list, yscrollcommand=scroller.set, width=400, height=150)
    scrollable_canvas.pack()

    scroller.config(command=scrollable_canvas.yview)

    scrollable_frame = tk.Frame(scrollable_canvas)
    scrollable_canvas.create_window((0, 0), window=scrollable_frame, anchor='nw', width=400)

    entry_name.bind("<KeyRelease>", on_key_return_entry)
    entry_name.property_name = "Name"

    entry_race.bind("<KeyRelease>", on_key_return_entry)
    entry_race.property_name = "Race"

    entry_class.bind("<KeyRelease>", on_key_return_entry)
    entry_class.property_name = "Class"

    entry_alignment.bind("<KeyRelease>", on_key_return_entry)
    entry_alignment.property_name = "Alignment"

    entry_level.bind("<KeyRelease>", on_key_return_entry)
    entry_level.property_name = "Level"

    entry_experience.bind("<KeyRelease>", on_key_return_entry)
    entry_experience.property_name = "Experience"

    entry_hit_points.bind("<KeyRelease>", on_key_return_entry)
    entry_hit_points.property_name = "HP"

    entry_armor_class.bind("<KeyRelease>", on_key_return_entry)
    entry_armor_class.property_name = "AC"

    entry_strength.bind("<KeyRelease>", on_key_return_entry)
    entry_strength.property_name = "Strength"

    entry_intelligence.bind("<KeyRelease>", on_key_return_entry)
    entry_intelligence.property_name = "Intelligence"

    entry_wisdom.bind("<KeyRelease>", on_key_return_entry)
    entry_wisdom.property_name = "Wisdom"

    entry_dexterity.bind("<KeyRelease>", on_key_return_entry)
    entry_dexterity.property_name = "Dexterity"

    entry_constitution.bind("<KeyRelease>", on_key_return_entry)
    entry_constitution.property_name = "Constitution"

    entry_charisma.bind("<KeyRelease>", on_key_return_entry)
    entry_charisma.property_name = "Charisma"

    text_skills.bind("<KeyRelease>", on_key_return_text)
    text_skills.property_name = "Skills"

    text_inventory.bind("<KeyRelease>", on_key_return_text)
    text_inventory.property_name = "Inventory"

    text_notes.bind("<KeyRelease>", on_key_return_text)
    text_notes.property_name = "Notes"

    frame_module_random_encounters = tk.Frame(root)

    label_random_encounter = tk.Label(frame_module_random_encounters)
    label_random_encounter.config(font=("Arial", 20), wraplength=500)
    label_random_encounter.pack()
    
    frame_random_encounter_row1 = tk.Frame(frame_module_random_encounters)
    frame_random_encounter_row1.pack()
    
    frame_random_encounter_column1 = tk.Frame(frame_random_encounter_row1)
    frame_random_encounter_column1.pack(side='left')
    
    button_random_biome = tk.Button(frame_random_encounter_column1, text="Random Biome", command=random_biome, width=20)
    button_random_biome.pack()

    button_random_terrain = tk.Button(frame_random_encounter_column1, text="Random Terrain", command=random_terrain, width=20)
    button_random_terrain.pack()

    button_random_weather = tk.Button(frame_random_encounter_column1, text="Random Weather", command=random_weather, width=20)
    button_random_weather.pack()
    
    frame_random_encounter_column2= tk.Frame(frame_random_encounter_row1)
    frame_random_encounter_column2.pack(side='left')

    button_random_event = tk.Button(frame_random_encounter_column2, text="Random Event", command=random_event, width=20)
    button_random_event.pack()

    button_random_npc = tk.Button(frame_random_encounter_column2, text="Random NPC", command=random_npc, width=20)
    button_random_npc.pack()
    
    button_random_treasure = tk.Button(frame_random_encounter_column2, text="Random Treasure", command=random_treasure, width=20)
    button_random_treasure.pack()

    button_random_trap = tk.Button(frame_random_encounter_column2, text="Ran dom Trap", command=random_trap, width=20)
    button_random_trap.pack()

    current_module_index = 0

    def toggle_module_visibility(direction):
        for frame in frame_modules:
            frame.pack_forget()

        nonlocal current_module_index

        if direction == 'left':
            current_module_index = (current_module_index - 1) % len(frame_modules)
        elif direction == 'right':
            current_module_index = (current_module_index + 1) % len(frame_modules)

        module_selection_var.set(frame_modules_text[current_module_index])

        module = frame_modules[current_module_index]
        module.pack(anchor='center', expand=True)

    frame_modules = [
        frame_module_dice_roller,
        frame_module_character_manager,
        frame_module_adventure_log,
        frame_module_monster_spawner,
        frame_module_random_encounters
    ]

    frame_modules_text = [
        "Dice Roller",
        "Character Manager",
        "Adventure Log",
        "Monster Spawner",
        "Random Encounters"
    ]

    module_selection_var = tk.StringVar(value=frame_modules_text[current_module_index])

    def change_module(selected_module):
        for frame in frame_modules:
            frame.pack_forget()

        module_selection_var.set(selected_module)
        selected_module_index = frame_modules_text.index(selected_module)
        frame_modules[selected_module_index].pack(anchor='center', expand=True)

    radio_dice_roller = tk.Radiobutton(frame_module_selection, text="Dice Roller", variable=module_selection_var, value="Dice Roller", command=lambda: change_module("Dice Roller"))
    radio_dice_roller.pack(side='left')

    radio_character_manager = tk.Radiobutton(frame_module_selection, text="Character Manager", variable=module_selection_var, value="Character Manager", command=lambda: change_module("Character Manager"))
    radio_character_manager.pack(side='left')

    radio_adventure_log = tk.Radiobutton(frame_module_selection, text="Adventure Log", variable=module_selection_var, value="Adventure Log", command=lambda: change_module("Adventure Log"))
    radio_adventure_log.pack(side='left')

    radio_monster_spawner = tk.Radiobutton(frame_module_selection, text="Monster Spawner", variable=module_selection_var, value="Monster Spawner", command=lambda: change_module("Monster Spawner"))
    radio_monster_spawner.pack(side='left')

    radio_random_encounters = tk.Radiobutton(frame_module_selection, text="Random Encounters", variable=module_selection_var, value="Random Encounters", command=lambda: change_module("Random Encounters"))
    radio_random_encounters.pack(side='left')

    root.bind("<Control-z>", lambda event: toggle_module_visibility('left'))
    root.bind("<Control-x>", lambda event: toggle_module_visibility('right'))
    root.bind("<Configure>", lambda e: scrollable_canvas.config(scrollregion=scrollable_canvas.bbox("all")))

    root.mainloop()
    
if __name__ == "__main__":
    main()


