# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1002

def calculate_the_circle_area(radius)
  3.14159 * (radius**2)
end

radius = gets.to_f
circle_area = calculate_the_circle_area(radius).to_f.round(4)

puts "A=#{circle_area}"
