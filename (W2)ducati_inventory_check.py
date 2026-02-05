with open("garage.txt", "r", encoding="utf-8") as input_file:
    with open("inventory_summary.txt", "w", encoding="utf-8") as output_file:
        output_file.write ("=== DUCATI V4 INVERNTORY ===\n")
        v4_count = 0  
        
        for line in input_file:
            
            data = line.strip().split(",")
            name = data[0]
            mileage = data[1]

            if "V4" in name:
                v4_count = v4_count + 1
            
                output_file.write(f"{v4_count}. {name}\n")
          
        
        output_file.write("=======================================\n")
        output_file.write(f"Total V4 Bikes: {v4_count}\n")
        if v4_count >= 15:
                rank = "High Performance"
        else:
                rank = "Standard"
        output_file.write(f"Garage Rank :{rank} \n")
        
        output_file.write("=======================================\n")
        output_file.write("Report by Thanawit (Software Engineer)\n")