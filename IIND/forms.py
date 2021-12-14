from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,validators
from wtforms.fields.core import FloatField, IntegerField
from wtforms.fields.simple import TextField

class matrixForm(FlaskForm):
    n1 = FloatField(label="n1",validators=[validators.optional()])
    n2 = FloatField(label="n2",validators=[validators.optional()])
    n3 = FloatField(label="n3",validators=[validators.optional()])
    n4 = FloatField(label="n4",validators=[validators.optional()])
    n5 = FloatField(label="n5",validators=[validators.optional()])
    n6 = FloatField(label="n6",validators=[validators.optional()])
    n7 = FloatField(label="n7",validators=[validators.optional()])
    n8 = FloatField(label="n8",validators=[validators.optional()])
    n9 = FloatField(label="n9",validators=[validators.optional()])
    n10 = FloatField(label="n10",validators=[validators.optional()])
    n11 = FloatField(label="n11",validators=[validators.optional()])
    n12 = FloatField(label="n12",validators=[validators.optional()])
    n13 = FloatField(label="n13",validators=[validators.optional()])
    n14 = FloatField(label="n14",validators=[validators.optional()])
    n15 = FloatField(label="n15",validators=[validators.optional()])
    n16 = FloatField(label="n16",validators=[validators.optional()])
    n17 = FloatField(label="n17",validators=[validators.optional()])
    n18 = FloatField(label="n18",validators=[validators.optional()])
    n19 = FloatField(label="n19",validators=[validators.optional()])
    n20 = FloatField(label="n20",validators=[validators.optional()])
    n21 = FloatField(label="n21",validators=[validators.optional()])
    n22 = FloatField(label="n22",validators=[validators.optional()])
    n23 = FloatField(label="n23",validators=[validators.optional()])
    n24 = FloatField(label="n24",validators=[validators.optional()])
    n25 = FloatField(label="n25",validators=[validators.optional()])
    s = SubmitField(label="Submit")

class crossProductForm(FlaskForm):
    u1 = FloatField("u1")
    u2 = FloatField("u2")
    u3 = FloatField("u3")
    v1 = FloatField("v1")
    v2 = FloatField("v2")
    v3 = FloatField("v3")
    s = SubmitField("Submit")

    def getVectors(self):
        u1 = self.u1.data
        u2 = self.u2.data
        u3 = self.u1.data
        v1 = self.v1.data
        v2 = self.v2.data
        v3 = self.v1.data

        return [[u1,u2,u3],[v1,v2,v3]]


class dotProductForm(FlaskForm):
    u1 = FloatField("u1",[validators.optional()])
    u2 = FloatField("u2",[validators.optional()])
    u3 = FloatField("u3",[validators.optional()])
    u4 = FloatField("u4",[validators.optional()])
    u5 = FloatField("u5",[validators.optional()])
    v1 = FloatField("v1",[validators.optional()])
    v2 = FloatField("v2",[validators.optional()])
    v3 = FloatField("v3",[validators.optional()])
    v4 = FloatField("v4",[validators.optional()])
    v5 = FloatField("v5",[validators.optional()])
    s = SubmitField("Submit")

    def getVectors(self):
        a1 = self.u1.data
        a2 = self.u2.data
        a3 = self.u3.data
        a4 = self.u4.data
        a5 = self.u5.data
        b1 = self.v1.data
        b2 = self.v2.data
        b3 = self.v3.data
        b4 = self.v4.data
        b5 = self.v5.data

        l1 = [a1,a2,a3,a4,a5]
        l2 = [b1,b2,b3,b4,b5]
        v1 = []
        v2 = []

        for i in range(len(l1)):
            if(l1[i] != None and l2[i] != None):
                
                v1.append(l1[i])
                v2.append(l2[i])
        
        return [v1,v2]
                
class systemForm(FlaskForm):
    n1 = FloatField(label="n1",validators=[validators.optional()])
    n2 = FloatField(label="n2",validators=[validators.optional()])
    n3 = FloatField(label="n3",validators=[validators.optional()])
    n4 = FloatField(label="n4",validators=[validators.optional()])
    n5 = FloatField(label="n5",validators=[validators.optional()])
    n6 = FloatField(label="n6",validators=[validators.optional()])
    n7 = FloatField(label="n7",validators=[validators.optional()])
    n8 = FloatField(label="n8",validators=[validators.optional()])
    n9 = FloatField(label="n9",validators=[validators.optional()])
    n10 = FloatField(label="n10",validators=[validators.optional()])
    n11 = FloatField(label="n11",validators=[validators.optional()])
    n12 = FloatField(label="n12",validators=[validators.optional()])
    n13 = FloatField(label="n13",validators=[validators.optional()])
    n14 = FloatField(label="n14",validators=[validators.optional()])
    n15 = FloatField(label="n15",validators=[validators.optional()])
    n16 = FloatField(label="n16",validators=[validators.optional()])
    n17 = FloatField(label="n17",validators=[validators.optional()])
    n18 = FloatField(label="n18",validators=[validators.optional()])
    n19 = FloatField(label="n19",validators=[validators.optional()])
    n20 = FloatField(label="n20",validators=[validators.optional()])
    n21 = FloatField(label="n21",validators=[validators.optional()])
    n22 = FloatField(label="n22",validators=[validators.optional()])
    n23 = FloatField(label="n23",validators=[validators.optional()])
    n24 = FloatField(label="n24",validators=[validators.optional()])
    n25 = FloatField(label="n25",validators=[validators.optional()])
    
    r1 = FloatField(label="r1",validators=[validators.optional()])
    r2 = FloatField(label="r2",validators=[validators.optional()])
    r3 = FloatField(label="r3",validators=[validators.optional()])
    r4 = FloatField(label="r4",validators=[validators.optional()])
    r5 = FloatField(label="r5",validators=[validators.optional()])

    s = SubmitField(label="Submit")

         


