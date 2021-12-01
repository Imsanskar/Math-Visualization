
const canvasWidth = 1800;
const canvasHeight = 1000;

let mainarr = [];

function myrotation(x,y,theta,fixedx = 0, fixedy = 0){
    rad = theta * Math.PI/180
    xplus = fixedx* (1-Math.cos(rad)) + fixedy * Math.sin(rad);
    yplus = fixedy*(1-Math.cos(rad)) - fixedx * Math.sin(rad);
    return [x*Math.cos(rad) - y*Math.sin(rad) + xplus, x*sin(rad)+y*cos(rad) + yplus];
    
  }

class Lsys
{
    constructor(x,y,size)
    {
        this.x = x;
        this.y = y;
        this.size = size;
        this.turn = 0;
    }

    //moveR
    moveR()
    {
        this.x += this.size;
    }
    //move left 
    //move up
    //move down
    moveD()
    {
        this.y += this.size;
        this.x = 100;
    }

    //draw right
    drawR()
    {
        
        strokeWeight(5);
        line(this.x, this.y, this.x+this.size, this.y);
        this.x += this.size;
    }

    //draw left
    drawL()
    {
        strokeWeight(5);
        line(this.x, this.y, this.x-this.size, this.y);
        this.x -= this.size;
    } 

    //draw up
    drawU()
    {
        strokeWeight(5);
        line(this.x, this.y, this.x, this.y - this.size);
        this.y -= this.size;
    }

    //draw down
    drawD()
    {
        strokeWeight(5);
        line(this.x, this.y, this.x, this.y + this.size);
        this.y += this.size;
    }

    //draw Forward
    drawF()
    {
    
        strokeWeight(5);
        let to = myrotation(this.x+this.size, this.y, this.turn, this.x, this.y);
        // line(this.x, this.y, to[0], to[1]);
        mainarr.push([this.x, this.y, to[0], to[1]]);
        this.x = to[0];
        this.y = to[1];
    }

    
};




function setup()
{
    createCanvas(canvasWidth, canvasHeight);
    hilb();

}

function hilb()
{
    let string = 'A'

    let prod_rules = {'A':'+BF-AFA-FB+','B':'-AF+BFB+FA-'} 

    let iterations = 7; //no of times the production rule must be replaced

    let temp = '';
    let size = 200;
    let xy = new Lsys(0,200, size);

    while(iterations>0)
    {
        //parse string()
        temp = '';
        for(let char of string)
        {
            //do lsystem function
            if(char == 'F')
            {
                //draw forward
                xy.drawF();
                temp+= 'F';
                // alert('hold');
            }

            if(char == '+')
            {
                //turn left 90 degrees
                xy.turn += 90;
                temp+= '+'

            }

            if(char == '-')
            {
                //turn right 90 degrees
                xy.turn -= 90;
                temp+= '-'
            }

            if(char == 'A')
            {
                //replace string according to production rules in temporary string
                temp += prod_rules[char];
            }
                

            if(char == 'B')
            {
                //replace string according to production rules
                temp += prod_rules[char];
            }
                
        }
    
            xy.moveR();
            string = temp; 
            //decrease size of the movement/draw
            xy.size /= 2;
            iterations--;
    }

}

let count = 0;
let delay = 200;

function draw(){

    background(220);
    // hilb();
    // alert('hilb')
    // alert('hold')
    delay = 200;
    delay++;
    if(delay>200)
    {
        for(let i=0; i<=count; i++)
        {
            
            line(mainarr[i][0], mainarr[i][1], mainarr[i][2], mainarr[i][3]);
        }
        count++;
       
        delay = 0;
        if(count==(mainarr.length))
        {
            count = 0;
        }
    }
  
}
