import tkinter as tk
from random import randint

def main():
    root = tk.Tk()
    root.title("Custom Tkinter App")
    root.resizable(False, False)

    adventures = ['New Adventure']
    adventure_variable = tk.StringVar(value=adventures[0])
    
    characters = {
        'New Campaign': 'New Character'
        }

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

        text_rolls.config(state=tk.NORMAL)
        text_rolls.insert(tk.END, '\n')
        text_rolls.insert(tk.END, f'Rolled {dice_rolls} {dice_multiplier}d{dice}:\n')
        for rolls, dice_sum in zip(all_rolls, all_sums):
            text_rolls.insert(tk.END, ', '.join(map(str, rolls)))
            if dice_multiplier > 1:
                text_rolls.insert(tk.END, f' = {dice_sum}\n')
            else:
                text_rolls.insert(tk.END, '\n')

        text_rolls.delete("end-2c", "end-1c")
        text_rolls.config(state=tk.DISABLED)
        text_rolls.yview_moveto(1.0)

    frame_column1 = tk.Frame(root)
    frame_column1.pack(side='left', expand=True, fill='both')

    frame_module_dice_roller = tk.Frame(frame_column1, borderwidth=1, relief='raised')
    frame_module_dice_roller.pack(expand=True, fill='both')

    frame4 = tk.Frame(frame_module_dice_roller)
    frame4.pack()

    label_dice_rolls = tk.Label(frame4, text="Rolls")
    label_dice_rolls.pack(side="left")

    entry_dice_rolls = tk.Entry(frame4, width=5)
    entry_dice_rolls.pack(side="left")

    label_dice_amount = tk.Label(frame4, text="Dice")
    label_dice_amount.pack(side="left")

    entry_dice_multiplier = tk.Entry(frame4, width=5)
    entry_dice_multiplier.pack(side="left")

    frame5 = tk.Frame(frame_module_dice_roller)
    frame5.pack()

    button_roll_d4 = tk.Button(frame5, text="d4", command=lambda: roll_dice(4))
    button_roll_d4.pack(side="left")

    button_roll_d6 = tk.Button(frame5, text="d6", command=lambda: roll_dice(6))
    button_roll_d6.pack(side="left")

    button_roll_d8 = tk.Button(frame5, text="d8", command=lambda: roll_dice(8))
    button_roll_d8.pack(side="left")

    button_roll_d10 = tk.Button(frame5, text="d10", command=lambda: roll_dice(10))
    button_roll_d10.pack(side="left")

    button_roll_d12 = tk.Button(frame5, text="d12", command=lambda: roll_dice(12))
    button_roll_d12.pack(side="left")

    button_roll_d20 = tk.Button(frame5, text="d20", command=lambda: roll_dice(20))
    button_roll_d20.pack(side="left")

    button_roll_d100 = tk.Button(frame5, text="d100", command=lambda: roll_dice(100))
    button_roll_d100.pack(side="left")

    frame6 = tk.Frame(frame_module_dice_roller)
    frame6.pack()
        
    text_rolls = tk.Text(frame6, width=40, height=7, wrap="word", state="disabled")
    text_rolls.pack()

    frame_module_character_manager = tk.Frame(frame_column1, borderwidth=1, relief='raised')
    frame_module_character_manager.pack(expand=True, fill='both')

    frame7 = tk.Frame(frame_module_character_manager)
    frame7.pack()

    label_campaign = tk.Label(frame7, text="Campaigns")
    label_campaign.pack(side="left")

    option_menu_campaign = tk.OptionMenu(frame7, None, "")
    option_menu_campaign.pack(side="left")

    button_new_campaign = tk.Button(frame7, text="New")
    button_new_campaign.pack(side="left")

    button_delete_campaign = tk.Button(frame7, text="Delete")
    button_delete_campaign.pack(side="left")

    button_rename_campaign = tk.Button(frame7, text="Rename")
    button_rename_campaign.pack(side="left")

    frame8 = tk.Frame(frame_module_character_manager)
    frame8.pack()

    label_character_label = tk.Label(frame8, text="Characters")
    label_character_label.pack(side="left")

    option_menu_character = tk.OptionMenu(frame8, None, "")
    option_menu_character.pack(side="left")

    button_new_character = tk.Button(frame8, text="New")
    button_new_character.pack(side="left")

    button_delete_character = tk.Button(frame8, text="Delete")
    button_delete_character.pack(side="left")

    button_save_character = tk.Button(frame8, text="Save")
    button_save_character.pack()

    frame9 = tk.Frame(frame_module_character_manager)
    frame9.pack()

    label_name_label = tk.Label(frame9, text="Name", width=10)
    label_name_label.pack(side="left")

    entry_name_entry = tk.Entry(frame9)
    entry_name_entry.pack(side="left")

    label_race_label = tk.Label(frame9, text="Race", width=10)
    label_race_label.pack(side="left")

    entry_race_entry = tk.Entry(frame9)
    entry_race_entry.pack(side="left")

    frame11 = tk.Frame(frame_module_character_manager)
    frame11.pack()

    label_class_label = tk.Label(frame11, text="Class", width=10)
    label_class_label.pack(side="left")

    entry_class_entry = tk.Entry(frame11)
    entry_class_entry.pack(side="left")

    label_alignment_label = tk.Label(frame11, text="Alignment", width=10)
    label_alignment_label.pack(side="left")

    entry_alignment_entry = tk.Entry(frame11)
    entry_alignment_entry.pack(side="left")

    frame13 = tk.Frame(frame_module_character_manager)
    frame13.pack()

    label_level_label = tk.Label(frame13, text="Level", width=5)
    label_level_label.pack(side="left")

    entry_level_entry = tk.Entry(frame13, width=5)
    entry_level_entry.pack(side="left")

    label_experience_label = tk.Label(frame13, text="Experience", width=10)
    label_experience_label.pack(side="left")

    entry_experience_entry = tk.Entry(frame13, width=15)
    entry_experience_entry.pack(side="left")

    label_hit_points_label = tk.Label(frame13, text="HP", width=3)
    label_hit_points_label.pack(side="left")

    entry_hit_points_entry = tk.Entry(frame13, width=5)
    entry_hit_points_entry.pack(side="left")

    label_armor_class_label = tk.Label(frame13, text="AC", width=3)
    label_armor_class_label.pack(side="left")

    entry_armor_class_entry = tk.Entry(frame13, width=5)
    entry_armor_class_entry.pack(side="left")

    frame17 = tk.Frame(frame_module_character_manager)
    frame17.pack()

    label_strength_label = tk.Label(frame17, text="Strength", width=10)
    label_strength_label.pack(side="left")

    entry_strength_entry = tk.Entry(frame17, width=5)
    entry_strength_entry.pack(side="left")

    label_intelligence_label = tk.Label(frame17, text="Intelligence", width=10)
    label_intelligence_label.pack(side="left")

    entry_intelligence_entry = tk.Entry(frame17, width=5)
    entry_intelligence_entry.pack(side="left")

    label_wisdom_label = tk.Label(frame17, text="Wisdom", width=10)
    label_wisdom_label.pack(side="left")

    entry_wisdom_entry = tk.Entry(frame17, width=5)
    entry_wisdom_entry.pack(side="left")

    frame20 = tk.Frame(frame_module_character_manager)
    frame20.pack()

    label_dexterity_label = tk.Label(frame20, text="Dexterity", width=10)
    label_dexterity_label.pack(side="left")

    entry_dexterity_entry = tk.Entry(frame20, width=5)
    entry_dexterity_entry.pack(side="left")

    label_constitution_label = tk.Label(frame20, text="Constitution", width=10)
    label_constitution_label.pack(side="left")

    entry_constitution_entry = tk.Entry(frame20, width=5)
    entry_constitution_entry.pack(side="left")

    label_charisma_label = tk.Label(frame20, text="Charisma", width=10)
    label_charisma_label.pack(side="left")

    entry_charisma_entry = tk.Entry(frame20, width=5)
    entry_charisma_entry.pack(side="left")

    frame20 = tk.Frame(frame_module_character_manager)
    frame20.pack()

    label_skills = tk.Label(frame20, text="Skills", width=10)
    label_skills.pack(side="left")

    text_skills = tk.Text(frame20, width=40, height=4)
    text_skills.pack(side="left")
    
    frame21 = tk.Frame(frame_module_character_manager)
    frame21.pack()

    label_inventory = tk.Label(frame21, text="Inventory", width=10)
    label_inventory.pack(side="left")

    text_inventory = tk.Text(frame21, width=40, height=4)
    text_inventory.pack(side="left")

    frame22 = tk.Frame(frame_module_character_manager)
    frame22.pack()

    label_notes = tk.Label(frame22, text="Notes", width=10)
    label_notes.pack(side="left")

    text_notes = tk.Text(frame22, width=40, height=4)
    text_notes.pack(side="left")

    frame_column2 = tk.Frame(root)
    frame_column2.pack(side='left', expand=True, fill='both')

    frame_module_adventure_log = tk.Frame(frame_column2, borderwidth=1, relief='raised')
    frame_module_adventure_log.pack(expand=True, fill='both')
    
    frame1 = tk.Frame(frame_module_adventure_log)
    frame1.pack()

    option_menu_adventure = tk.OptionMenu(frame1, adventure_variable, *adventures)
    option_menu_adventure.pack(side='left')

    button_new_adventure = tk.Button(frame1, text="New")
    button_new_adventure.pack(side='left')

    button_delete_adventure = tk.Button(frame1, text="Delete")
    button_delete_adventure.pack(side='left')

    button_rename_adventure = tk.Button(frame1, text="Rename")
    button_rename_adventure.pack(side='left')

    frame2 = tk.Frame(frame_module_adventure_log)
    frame2.pack()

    label_day = tk.Label(frame2, text="Day:")
    label_day.pack(side='left')

    entry_day = tk.Entry(frame2, width=5)
    entry_day.pack(side='left')

    label_hour = tk.Label(frame2, text="Hour:")
    label_hour.pack(side='left')

    entry_hour = tk.Entry(frame2, width=5)
    entry_hour.pack(side='left')

    frame3 = tk.Frame(frame_module_adventure_log)
    frame3.pack()

    label_log = tk.Label(frame3, text="Log")
    label_log.pack(side='left')

    text_log = tk.Text(frame3, width=60, height=12)
    text_log.pack(side='left')

    frame_module_monster_spawner = tk.Frame(frame_column2, borderwidth=1, relief='raised')
    frame_module_monster_spawner.pack(expand=True, fill='both')

    frame25 = tk.Frame(frame_module_monster_spawner)
    frame25.pack()

    label_monster_type = tk.Label(frame25, text="Monster type")
    label_monster_type.pack(side="left")
    
    option_menu_monster_type = tk.OptionMenu(frame25, None, "")
    option_menu_monster_type.pack(side="left")

    button_add_monster = tk.Button(frame25, text="Add")
    button_add_monster.pack(side="left")

    button_add_monster_custom = tk.Button(frame25, text="Add Custom")
    button_add_monster_custom.pack(side="left")

    frame26 = tk.Frame(frame_module_monster_spawner)
    frame26.pack()

    label_monster_id = tk.Label(frame26, text="Monster ID")
    label_monster_id.pack(side="left")

    option_menu_monster_id = tk.OptionMenu(frame26, None, "")
    option_menu_monster_id.pack(side="left")

    button_delete_monster = tk.Button(frame26, text="Remove")
    button_delete_monster.pack(side="left")

    frame26 = tk.Frame(frame_module_monster_spawner, borderwidth=1, relief="solid")
    frame26.pack()

    scroller = tk.Scrollbar(frame26, orient=tk.VERTICAL)
    scroller.pack(side='right', fill='y')

    scrollable_canvas = tk.Canvas(frame26, yscrollcommand=scroller.set, width=400, height=150)
    scrollable_canvas.pack()

    scroller.config(command=scrollable_canvas.yview)

    scrollable_frame = tk.Frame(scrollable_canvas)
    scrollable_canvas.create_window((0, 0), window=scrollable_frame, anchor='nw', width=600)

    for i in range(8):
        inner_frame = tk.Frame(scrollable_frame, borderwidth=1, relief='groove')
        inner_frame.pack(expand=True, fill='x')
        
        label1 = tk.Label(inner_frame, text=i+1)
        label1.pack(side='left', padx=2)

        label2 = tk.Label(inner_frame, text='Monster')
        label2.pack(side='left', padx=2)
        
        entry3 = tk.Entry(inner_frame)
        entry3.pack(side='left', expand=True, fill='x')
        entry3.insert(0, 'HP / AC / Note')

    root.bind("<Configure>", lambda e: scrollable_canvas.config(scrollregion=scrollable_canvas.bbox("all")))

    root.mainloop()
    
if __name__ == "__main__":
    main()
