from rest_framework import serializers
from predicteur_app.models import Patient


class PatientSerializer(serializers.Serializer)  :
    """ to serialize or deserialize data
    -> Serialize                               : model instance / querysets => native Python datatypes => JSON
        ** NETWORK **
    -> Deserialize                             : JSON to model instance
    """
    
    chest_ACC_x        = serializers.FloatField()
    chest_ACC_y        = serializers.FloatField()
    chest_ACC_z        = serializers.FloatField()
    chest_Resp         = serializers.FloatField()
    chest_ECG          = serializers.FloatField()
    wrist_ACC_x        = serializers.FloatField()
    wrist_ACC_y        = serializers.FloatField()
    wrist_ACC_z        = serializers.FloatField()
    wrist_BVP          = serializers.FloatField()
    wrist_TEMP         = serializers.FloatField()
    WEIGHT             = serializers.FloatField()
    Gender             = serializers.FloatField()
    AGE                = serializers.FloatField()
    HEIGHT             = serializers.FloatField()
    SKIN               = serializers.FloatField()
    SPORT              = serializers.FloatField()
    Rpeaks             = serializers.FloatField()
    Label              = serializers.FloatField()
    Activity           = serializers.FloatField(allow_null=True)

    def create(self, validated_data)           :
        """ Create and return a new 'Patient' instance, given the validated data """
        return Patient.objects.create(**validated_data)

    def update(self, instance, validated_data) :
        """ Update and return an existing 'Patient' instance, given the validated data """
        instance.chest_ACC_x        = validated_data.get('chest_ACC_x' , instance.chest_ACC_x)
        instance.chest_ACC_y        = validated_data.get('chest_ACC_y' , instance.chest_ACC_y)
        instance.chest_ACC_z        = validated_data.get('chest_ACC_z' , instance.chest_ACC_z)
        instance.chest_Resp         = validated_data.get('chest_Resp' , instance.chest_Resp)
        instance.chest_ECG          = validated_data.get('chest_ECG' , instance.chest_ECG)
        instance.wrist_ACC_x        = validated_data.get('wrist_ACC_x' , instance.wrist_ACC_x)
        instance.wrist_ACC_y        = validated_data.get('wrist_ACC_y' , instance.wrist_ACC_y)
        instance.wrist_ACC_z        = validated_data.get('wrist_ACC_z' , instance.wrist_ACC_z)
        instance.wrist_BVP         = validated_data.get('wrist_BVP' , instance.wrist_BVP)
        instance.wrist_TEMP        = validated_data.get('wrist_TEMP' , instance.wrist_TEMP)
        instance.WEIGHT            = validated_data.get('WEIGHT' , instance.WEIGHT)
        instance.Gender            = validated_data.get('Gender' , instance.Gender)
        instance.AGE               = validated_data.get('AGE' , instance.AGE)
        instance.HEIGHT            = validated_data.get('HEIGHT' , instance.HEIGHT)
        instance.SKIN              = validated_data.get('SKIN' , instance.SKIN)
        instance.SPORT             = validated_data.get('SPORT' , instance.SPORT)
        instance.Rpeaks            = validated_data.get('Rpeaks' , instance.Rpeaks)
        instance.Label             = validated_data.get('Label' , instance.Label)
        #instance.Activity         = validated_data.get('Activity' , instance.Activity)
        
        instance.save()
        return instance