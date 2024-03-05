def draw_line(screen, width, x1, x2, y):
  #find the first full byte since x1.
  start_offset = x1%8
  first_full_byte = x1//8
  if start_offset != 0:
    first_full_byte+=1

  #find the last full byte before x2.
  end_offset = x2%8
  last_full_byte = x2//8
  #  [0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], 16, 17
  # x2= 15 
  # end_offset = 15%8 = 7
  # last_full_byte = 11//8 = 1
  if end_offset !=7:
    last_full_byte +=1

  # change all bytes to 0 from first_full_byte to last_full_byte
  bytes_per_line = (width/8)
  for b in range(first_full_byte, last_full_byte+1):
    screen[bytes_per_line*y+b]= 0xFF

  #create mastk for start end end of line. 
  start_mask = 0xFF>>start_offset
  end_mask = ~(0xFF>>(end_offset+1))

  # set start and end of line. 
  if (x1//8)==(x2//8):
    # if they are in the same byte.
    mask = start_mask & end_mask
    screen[bytes_per_line*y+(x1//8)]|=mask
  else:
    if start_offset!=0:
      byte_number = bytes_per_line + first_full_byte-1
      screen[byte_number]|=start_mask
    if end_offset!=7:
      byte_number = bytes_per_line + last_full_byte +1
      screen[byte_number]|=end_mask
  return screen
  
  