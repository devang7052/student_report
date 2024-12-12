from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,PageBreak
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from datetime import datetime
import numpy as np

def create_first_page(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by, story, styles):
    
    # Header with Logo and Company Name
    header_data = [[
        Image('hyperlab_logo.png', width=1.2*inch, height=0.5*inch),
        Paragraph(
            "<font color='#2E4053' size='16'><b>Hyperlab Sportech Pvt. Ltd. </b></font><br/>"
            "<font color='#5D6D7E' size='10'>Advanced Performance Assessment</font>",
            styles['Normal']
        )
    ]]
    header_table = Table(header_data, colWidths=[1.5*inch, 5.5*inch])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (1, 0), (1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(header_table)
    
    # Decorative Line
    line_table = Table([['']], colWidths=[7.5*inch], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
    ]))
    story.append(line_table)
    
    story.append(Spacer(1, 20))
    
    # Title Style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=12,
        textColor=colors.HexColor('#2E4053')
    )
    
    intro_paragraph_style = ParagraphStyle(
        'IntroParagraph',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceBefore=6,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )

    # Title
    story.append(Paragraph("Cardiovascular Health Assessment Report", title_style))
    
    # Information table
    info_data = [
        ["Student Name:", student_name, "Date of Assessment:", assessment_date],
        ["Device Used:", device_used, "Assessment Type:", drill_type],
        ["Test Duration:", test_duration, "Assessed by:", assessed_by]
    ]
    
    info_table = Table(info_data, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    info_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F4F6F7')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#F4F6F7')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 20))

    # Introduction Section
    story.append(Paragraph("Introduction", section_title_style))
    
    # intro_text = """The <b>Cardiovascular Health Assessment</b>, powered by HyperLab's HELIOS technology, is a comprehensive evaluation system designed to measure three critical aspects of cardiovascular fitness: <b>aerobic endurance</b>, <b>cardiovascular efficiency</b>, and <b>fatigue resistance</b>. This assessment utilizes advanced sensor technology to create a standardized testing environment that challenges participants through a series of precisely measured movements while monitoring heart rate responses and movement patterns."""
    intro_text="""The <b>Cardiovascular Health Drill</b> is designed to evaluate an athlete's endurance, speed consistency, and fatigue levels. This drill requires the athlete to move quickly between two points at set angles, with their speed and reaction times recorded at each iteration. It uses a speed threshold to track when the athlete’s speed falls below a target, marking potential fatigue points. The drill also includes heart rate monitoring, flagging fatigue when the heart rate reaches 1.5 times the resting rate."""
    story.append(Paragraph(intro_text, intro_paragraph_style))
    
    story.append(Spacer(1, 1))
    
    # intro_text2 = """This assessment provides detailed insights into an individual's cardiovascular health by measuring their ability to: maintain consistent movement speeds, regulate heart rate under progressive stress, and resist fatigue during sustained activity. These metrics are fundamental to both athletic performance and general health, making this assessment valuable for establishing baseline fitness levels, tracking progress, and identifying areas for targeted improvement in cardiovascular conditioning."""
    intro_text2="""Through this combination of speed and heart rate data, the drill provides insights into the athlete’s cardiovascular performance and endurance capacity. This report offers personalized feedback, showing strengths and areas for improvement based on their endurance, speed stability, and fatigue resistance, helping athletes to understand and target the specific areas for cardiovascular training."""
    story.append(Paragraph(intro_text2, intro_paragraph_style))
    
    story.append(Spacer(1, 15))

    # Procedure Section with branded header
    procedure_header = Table(
        [[Paragraph("Drill Structure and Procedure", section_title_style)]],
        colWidths=[7.5*inch],
        rowHeights=[40]
    )
    procedure_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(procedure_header)
    story.append(Spacer(1, 10))
    
    procedure_data=[
    ["Step", "Phase", "Procedure"],
    [
        "1. Setup",
        "System Initialization",
        "Home position setting"
    ],
    [
        "2. Movement Pattern",
        "Bilateral Target Setup",
        "Two fixed points at ±75°\n3000mm radius movement\n50 maximum iterations"
    ],
    [
        "3. Performance Metrics",
        "Real-time Monitoring",
        "Speed calculation in km/h\nMoving average computation\nHeart rate monitoring"
    ],
    [
        "4. Fatigue Analysis",
        "Adaptive Monitoring",
        "Speed threshold tracking\nAutomatic warning system"
    ],
    [
        "5. Data Collection",
        "Comprehensive Tracking",
        "Continuous tap detection"
    ],
    [
        "6. Assessment Completion",
        "System Shutdown",
        "Automatic termination check\nSystem deactivation sequence"
    ]
    ]
    
    procedure_table = Table(procedure_data, colWidths=[1.75*inch, 2.5*inch, 2*inch])
    procedure_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F4F6F7')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(procedure_table)

    return story

def calculate_performance_metrics(data):
    """Calculate enhanced performance metrics"""
    metrics = {}
    
    total_points = 50  # Total target points
    completed_points = len(data['speeds'])  # Actually completed points
    
    # 1. Speed Performance Analysis
    metrics['speed'] = {
        'average_speed': data['avgSpeed'],
        'peak_speed': data['highSpeed'],
        'minimum_speed': data['lowSpeed'],
        'speed_variation': round(np.std(data['speeds']), 2),
        'speed_consistency': round((1 - np.std(data['speeds'])/np.mean(data['speeds'])) * 100, 1),
        'completion_percentage': round((completed_points / total_points) * 100, 1)
    }
    
    # 2. Heart Rate Analysis
    metrics['heart_rate'] = {
        'average_hr': round(np.mean(data['heartrate']), 1),
        'peak_hr': max(data['heartrate']),
        'min_hr': min(data['heartrate']),
        'hr_range': f"{max(data['heartrate'])} - {min(data['heartrate'])}",
        'hr_stability': round(np.std(data['heartrate']), 1),
        'hrri':data['timestamp'][data['heartrate'].index(max(data['heartrate']))] - data['timestamp'][data['heartrate'].index(min(data['heartrate']))],
        'recovery_rate':min(1,abs((data['heartrate'][-1]-data['heartrate_after90'])/20))*10
    }

    # 3. Enhanced Fatigue Analysis
    speed_trend = np.polyfit(data['speedTimes'], data['speeds'], 1)[0]
    
    # Calculate Endurance Index (0-100)
    endurance_score = (completed_points / total_points) * 100
    speed_maintenance = (np.mean(data['speeds'][-3:]) / np.mean(data['speeds'][:3])) * 100
    hr_control = (1 - (len([hr for hr in data['heartrate'] if hr > data['heartrate'][0]*1.5]) / len(data['heartrate']))) * 100
    
    metrics['fatigue'] = {
        'endurance_score': round(endurance_score, 1),
        'fatigue_intensity': len(data['speeds'])/5,
        'speed_maintenance': round(speed_maintenance, 1),
        'hr_control_score': round(hr_control, 1),
        'completion_points': completed_points,
        'speed_degradation': round(speed_trend * 100, 2),
        'fatigue_onset_point': completed_points
    }
    
    return metrics
def add_colored_table_style(table,data, first_row_color='#2E4053', row_colors=['#F4F6F7', '#FFFFFF']):  
    """
    Adds professional styling to tables
    
    Parameters:
    table: ReportLab Table object
    first_row_color: Header row color (hex)
    row_colors: Alternating colors for data rows (hex)
    """
    row_count=len(data)
    style = [
        # Header row styling
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor(first_row_color)),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        
        # Data rows styling
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor(row_colors[0])),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2E4053')),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        
        # Grid styling
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('LINEBEFORE', (0, 0), (0, -1), 1, colors.HexColor('#E8E8E8')),
        ('LINEAFTER', (-1, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('LINEBELOW', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('LINEABOVE', (0, 0), (-1, 0), 1, colors.HexColor('#E8E8E8'))
    ]
    
    # Add alternating row colors
    for i in range(1, row_count):
        if i % 2 == 1:
            style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor(row_colors[0])))
        else:
            style.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor(row_colors[1])))
    
    table.setStyle(TableStyle(style))
    return table

def create_recommendations_page(story, styles, metrics):
    """Creates an enhanced personalized recommendations page focused on HRRI, Fatigue Intensity, and Recovery Rate"""
    story.append(PageBreak())
    
    # Enhanced Style definitions
    title_style = ParagraphStyle(
        'RecommendationsTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    section_style = ParagraphStyle(
        'RecommendationSection',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    description_style = ParagraphStyle(
        'RecommendationDescription',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )

    # Page Title with decorative elements
    title_box = Table(
        [[Paragraph("Training Recommendations", title_style)]],
        colWidths=[7*inch],
        rowHeights=[50]
    )
    title_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053')),
    ]))
    story.append(title_box)
    story.append(Spacer(1, 15))
    
    # Performance Summary Box
    summary = create_performance_summary_new(metrics)
    summary_box = Table(
        [[Paragraph(summary, description_style)]],
        colWidths=[7*inch]
    )
    summary_box.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#EBF5FB')),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#3498DB')),
    ]))
    story.append(summary_box)
    story.append(Spacer(1, 20))

    # Generate recommendations based on metrics
    recommendations = generate_targeted_recommendations(metrics)
    i = 0
    
    # Create recommendation boxes for each category
    for category, recs in recommendations.items():
        # Add page break after second category
        if i == 2:
            story.append(PageBreak())
            
        # Category header
        header_content = Table([
            [
                Paragraph(category, section_style)
            ]
        ], colWidths=[7*inch])
        
        header_table = Table(
            [[header_content]],
            colWidths=[7*inch],
            rowHeights=[45]
        )
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ]))
        story.append(header_table)
        
        # Create exercise recommendations table
        exercise_data = [["Exercise", "Duration", "Benefits", "Key Focus"]]
        for exercise in recs:
            exercise_data.append([
                Paragraph(f"<b>{exercise['name']}</b><br/>{exercise['prescription']}", description_style),
                Paragraph(exercise['prescription'], description_style),
                Paragraph(exercise['benefits'], description_style),
                Paragraph(exercise['notes'], description_style)
            ])
        
        exercise_table = Table(exercise_data, colWidths=[1.75*inch, 1.25*inch, 2*inch, 2*inch])
        exercise_table = add_colored_table_style(exercise_table, exercise_data, 
                                               first_row_color='#34495E',
                                               row_colors=['#F8F9F9', '#FFFFFF'])
        story.append(exercise_table)
        story.append(Spacer(1, 15))
        i += 1

    # Weekly Planning Guide
    story.append(Paragraph("Weekly Training Structure", section_style))
    weekly_plan = create_weekly_plan(metrics)
    story.append(weekly_plan)
    story.append(Spacer(1, 15))
    
    # Additional Notes
    notes_style = ParagraphStyle(
        'Notes',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#2E4053')
    )
    
    notes_text = """
    <b>Important Training Guidelines:</b>
    • Monitor your heart rate during all sessions
    • Focus on proper breathing techniques
    • Track your recovery time between sessions
    • Maintain consistent hydration levels
    • Record your HRRI progress regularly
    • Adjust intensity based on fatigue levels
    • Get adequate sleep for optimal recovery
    """
    
    notes_table = Table([[Paragraph(notes_text, notes_style)]], colWidths=[7*inch])
    notes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(notes_table)
    
    return story


def create_performance_summary_new(metrics):
    """Creates a personalized performance summary based on HRRI, Fatigue Intensity, and Recovery Rate"""
    hrri = metrics['heart_rate']['hrri']
    fatigue_intensity = metrics['fatigue']['fatigue_intensity']
    recovery_rate = metrics['heart_rate']['recovery_rate']
    
    summary = f"""<b>Your Performance Profile</b><br/>
    Based on your assessment results, your cardiovascular profile shows:
    • Heart Rate Recovery Index (HRRI): {hrri:.1f} minutes - {get_hrri_description(hrri)}
    • Fatigue Intensity Score: {fatigue_intensity:.1f}/10 - {get_fatigue_description(fatigue_intensity)}
    • Recovery Rate: {recovery_rate:.1f} min - {get_recovery_description(recovery_rate)}
    
    The following recommendations are tailored to enhance your cardiovascular efficiency and recovery capacity."""
    
    return summary

def get_hrri_description(hrri):
    if hrri <= 3:
        return "Excellent cardiac efficiency"
    elif hrri <= 5:
        return "Good cardiac response"
    elif hrri <= 7:
        return "Moderate cardiac adaptation"
    else:
        return "Needs improvement in cardiac recovery"

def get_fatigue_description(score):
    if score >= 8:
        return "High endurance capacity"
    elif score >= 6:
        return "Good stamina level"
    elif score >= 4:
        return "Moderate endurance"
    else:
        return "Basic endurance level"

def get_recovery_description(rate):
    if rate <= 2:
        return "Rapid recovery capacity"
    elif rate <= 4:
        return "Effective recovery pattern"
    elif rate <= 6:
        return "Moderate recovery ability"
    else:
        return "Extended recovery needed"

def create_performance_summary(metrics):
    """Creates a personalized performance summary"""
    endurance_score = metrics['fatigue']['endurance_score']
    hr_control = metrics['fatigue']['hr_control_score']
    speed_consistency = metrics['speed']['speed_consistency']
    
    summary = f"""<b>Your Performance Profile</b><br/>
    Based on your assessment results, your overall cardiovascular fitness profile shows:
    • Endurance Capacity: {get_performance_description(endurance_score)}
    • Heart Rate Control: {get_performance_description(hr_control)}
    • Movement Efficiency: {get_performance_description(speed_consistency)}
    
    The following recommendations are tailored to maintain your strengths and improve specific areas for optimal performance."""
    
    return summary

def get_performance_description(score):
    if score >= 90:
        return f"Exceptional ({score}%) - Maintain excellence"
    elif score >= 75:
        return f"Strong ({score}%) - Fine-tune performance"
    elif score >= 60:
        return f"Good ({score}%) - Room for improvement"
    else:
        return f"Developing ({score}%) - Focus area"



def generate_targeted_recommendations(metrics):
    """Generates recommendations based on HRRI, Fatigue Intensity, and Recovery Rate"""
    recommendations = {
        "Heart Rate Recovery (HRRI)": [
            {
                "name": "Interval Breathing",
                "prescription": "3 sets of 10 breaths",
                "benefits": "Improves heart rate recovery and cardiac efficiency",
                "notes": "Box breathing pattern: 4s inhale, 4s hold, 4s exhale"
            },
            {
                "name": "Active Recovery",
                "prescription": "10-15 minutes post-workout",
                "benefits": "Enhances heart rate recovery time",
                "notes": "Light jogging followed by dynamic stretches"
            },
            {
                "name": "Heart Rate Training",
                "prescription": "20-30 minutes",
                "benefits": "Builds cardiac efficiency",
                "notes": "Alternate between high and low intensity zones"
            }
        ],
        "Fatigue Management": [
            {
                "name": "Progressive Loading",
                "prescription": "3-4 sessions per week",
                "benefits": "Builds fatigue resistance",
                "notes": "Gradually increase duration and intensity"
            },
            {
                "name": "Recovery Circuit",
                "prescription": "15-20 minutes",
                "benefits": "Improves stamina and endurance",
                "notes": "Mix of low-impact cardio and mobility work"
            },
            {
                "name": "Endurance Building",
                "prescription": "30-45 minutes",
                "benefits": "Increases overall stamina",
                "notes": "Focus on steady-state cardio activities"
            }
        ],
        "Recovery Enhancement": [
            {
                "name": "Cool Down Protocol",
                "prescription": "10-15 minutes post-exercise",
                "benefits": "Optimizes recovery rate",
                "notes": "Gradual reduction in intensity with stretching"
            },
            {
                "name": "Recovery Breathing",
                "prescription": "5-10 minutes",
                "benefits": "Accelerates heart rate normalization",
                "notes": "Deep diaphragmatic breathing exercises"
            },
            {
                "name": "Active Mobility",
                "prescription": "15-20 minutes",
                "benefits": "Enhances recovery capacity",
                "notes": "Dynamic stretching and mobility drills"
            }
        ]
    }
    
    return recommendations

def create_weekly_plan(metrics):
    """Creates a detailed weekly training plan focused on HRRI and recovery"""
    plan_data = [
        ["Day", "Primary Focus", "Specific Exercises", "Duration", "Notes"],
        ["Monday", "HRRI Training", 
         "• Interval Training\n• Recovery Breathing\n• Cool Down", 
         "40-45 min", 
         "Focus on breath control"],
        
        ["Tuesday", "Recovery Focus",
         "• Light Cardio\n• Mobility Work\n• Stretching",
         "30-35 min",
         "Emphasis on technique"],
        
        ["Wednesday", "Active Recovery",
         "• Walking\n• Dynamic Stretching\n• Breathing Exercises",
         "25-30 min",
         "Keep intensity low"],
        
        ["Thursday", "Fatigue Management",
         "• Circuit Training\n• Recovery Drills\n• Cool Down",
         "40-45 min",
         "Monitor heart rate"],
        
        ["Friday", "HRRI Development",
         "• Interval Work\n• Recovery Protocol\n• Breathing Work",
         "35-40 min",
         "Focus on recovery"],
        
        ["Saturday", "Endurance",
         "• Steady State Cardio\n• Active Recovery\n• Cool Down",
         "30-35 min",
         "Maintain consistent pace"],
        
        ["Sunday", "Complete Recovery",
         "• Light Walking\n• Stretching\n• Breathing Work",
         "20-25 min",
         "Focus on relaxation"]
    ]
    
    # Create table with enhanced styling
    plan_table = Table(plan_data, colWidths=[1*inch, 1.45*inch, 2*inch, 1.25*inch, 1.7*inch])
    plan_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9F9')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2E4053')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('PADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#EBF5FB')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#EBF5FB')),
        ('BACKGROUND', (0, 6), (-1, 6), colors.HexColor('#EBF5FB')),
    ]))
    
    return plan_table


def create_important_notes():
    """Creates comprehensive notes section with practical guidelines"""
    notes_text = """
    <b>Essential Training Guidelines:</b>
    
    1. Warm-Up Protocol (10-15 minutes):
       • 5 minutes light cardio (jogging, jumping jacks, or jump rope)
       • Dynamic stretches (leg swings, arm circles, hip rotations)
       • Movement preparation specific to your workout
    
    2. Exercise Progression:
       • Begin at 70% of suggested intensity for first week
       • Increase duration before increasing intensity
       • Add one set or 5 minutes to exercises every 2 weeks
       • Monitor heart rate recovery between sets
    
    3. Form and Technique:
       • Maintain proper posture during all exercises
       • Focus on controlled movements rather than speed
       • Use mirrors when available to check form
       • Record exercises occasionally to review technique
    
    4. Recovery Strategies:
       • Ensure 7-8 hours of sleep daily
       • Stay hydrated (minimum 3 liters water daily)
       • Use foam rolling for muscle recovery
       • Take complete rest day if experiencing unusual fatigue
    
    5. Heart Rate Monitoring:
       • Use 220-age formula for max heart rate estimation
       • Recovery heart rate should return to below 120 BPM within 2 minutes
       • Monitor morning resting heart rate for overtraining
       • Keep heart rate within prescribed zones during sessions
    
    6. Safety Considerations:
       • Stop exercise if experiencing dizziness or unusual pain
       • Adjust intensity during extreme weather conditions
       • Wear appropriate footwear and breathable clothing
       • Keep exercise space well-ventilated
    
    7. Progress Tracking:
       • Log all workouts in a fitness app or journal
       • Take progress photos every 4 weeks
       • Reassess performance metrics monthly
       • Update training plan based on progress
    
    8. Nutrition Timing:
       • Eat light meal 2-3 hours before training
       • Post-workout nutrition within 30 minutes
       • Stay hydrated before, during, and after exercise
       • Adjust caloric intake based on training intensity

    <b>Common Exercise Resources:</b>
    • YouTube: Search for "proper form" videos of specific exercises
    • Mobile Apps: Nike Training Club, Strava for tracking
    • Websites: ExRx.net for exercise library
    • Fitness Blogs: Runner's World, ACE Fitness for tips
    """
    return notes_text

def create_score_understanding_page(story, styles, results):
    """Creates the score understanding section with structured metric explanations"""
    metrics=calculate_performance_metrics(results)
    # Add page break
    story.append(PageBreak())
    
    # Title Style
    title_style = ParagraphStyle(
        'UnderstandingTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Section Style
    section_style = ParagraphStyle(
        'MetricSection',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    # Metric name style
    metric_name_style = ParagraphStyle(
        'MetricName',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#2E4053'),
        fontName='Helvetica-Bold'
    )
    
    # Description style
    description_style = ParagraphStyle(
        'MetricDescription',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Page Title
    story.append(Paragraph("Understanding Your Scores", title_style))
    story.append(Spacer(1, 20))
    
    # Introduction text
    intro_text = """This section provides a detailed explanation of each metric used in your cardiovascular assessment. Understanding these metrics will help you interpret your performance and identify areas for improvement. Each metric has been carefully designed to measure specific aspects of your cardiovascular fitness during the endurance drill."""
    
    story.append(Paragraph(intro_text, description_style))
    story.append(Spacer(1, 20))
    
    # Define metrics data
    metrics_data = [
        {
            "title": "HRRI",
            "description": """Heart rate recovery index is the time taken by heart rate to reach its maximum value at\nwhich fatigue of athlete will start""",
            "calculation": "(max_heart_rate_timestamp-starting_heart_rate_timestamp)",
            "your_score": f"{metrics['heart_rate']['hrri']:.1f} min"
        },
        {
            "title": "Fatigue Intensity",
            "description": """Its the overall score that tells how much endurance power do you have to complete the drill""",
            "calculation": "total_tap_points/5",
            "your_score": f"{metrics['fatigue']['fatigue_intensity']:.1f}"
        },

        {
            "title": "Recovery Rate",
            "description": """Evaluates how fast you can recover from the fatigue level""",
            "calculation": "(min(1,(heart_rate_at_end_of_the_drill-heart_rate_after_90_sec))/20)*10",
            "your_score": f"{metrics['heart_rate']['recovery_rate']:.1f} min"
        }
    ]

    # Create metric sections
    i = 0
    for metric in metrics_data:
        if i == 4:
            story.append(PageBreak())
            
        # Metric Header
        header_table = Table(
            [[Paragraph(metric["title"], metric_name_style)]],
            colWidths=[7*inch],
            rowHeights=[30]
        )
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
        ]))
        story.append(header_table)
        
        # Create content table
        content_data = [
            ["Description:", metric["description"]],
            ["Calculation:", metric["calculation"]],
            ["Your Score:", metric["your_score"]],
            # ["Interpretation:", "\n".join([f"{k}: {v}" for k, v in metric["interpretation"].items()])]
        ]
        
        content_table = Table(content_data, colWidths=[1.5*inch, 5.5*inch])
        content_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F8F9F9')),
        ]))
        
        story.append(content_table)
        story.append(Spacer(1, 15))
        i += 1

    # Additional Information Section
    story.append(Paragraph("Additional Notes", section_style))
    
    notes_text = """
    • HRR(heart rate reserve) is the fatigue point of the athlete after this athlete can't push his limits anymore.  
    • Fatigue detection uses both physical movement and cardiovascular response patterns.
    • Heart rate is continuously monitored to assess cardiovascular efficiency.
    • Performance is monitored across 50 points or until fatigue threshold is reached.
    """
    
    notes_table = Table([[Paragraph(notes_text, description_style)]], colWidths=[7*inch])
    notes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 12),
    ]))
    
    story.append(notes_table)
    
    return story

def create_metrics_page(story, styles, performance_data):
    """Creates enhanced performance metrics section"""
    metrics = calculate_performance_metrics(performance_data)
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceBefore=20,
        spaceAfter=12,
        textColor=colors.HexColor('#2E4053')
    )
    
    subsection_style = ParagraphStyle(
        'SubSection',
        parent=styles['Heading3'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#34495E')
    )
    
    metric_description_style = ParagraphStyle(
        'MetricDescription',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        spaceBefore=6,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )

    # Main Page Heading
    main_title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceBefore=20,
        spaceAfter=20,
        textColor=colors.HexColor('#2E4053'),
        alignment=1  # Center alignment
    )    
    story.append(PageBreak())
    story.append(Paragraph("Performance Summary", main_title_style))
    
    # Assessment Level Box with Graphical Elements
    level_data = get_assessment_level(metrics['fatigue']['fatigue_intensity'])
    assessment_content = [
        [Paragraph(f"""
        <font color='{level_data['color']}' size='11'><b>{level_data['level']}</b></font>
        <br/>
        <font color="#7F8C8D" size='8'><b>Overall Score: {metrics['fatigue']['fatigue_intensity']:.1f}/10</b></font>    
        <br/>
        <font color='#5D6D7E' size='9'>Assessment based on overall performance metrics</font>
        """, styles['Normal'])]
    ]
    
    assessment_box = Table(assessment_content, colWidths=[6*inch])
    assessment_box.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(assessment_box)
    story.append(Spacer(1, 10))

    # 1. Movement Performance Analysis
    story.append(Paragraph("Performance Parameters", section_title_style))
    
    # Add completion rate to movement metrics
    movement_data = [
        ["Parameter", "Measured Value","Description"],
        ["Completion Rate", f"{metrics['speed']['completion_percentage']}%","% of drill completed"],
        ["Average Speed", f"{metrics['speed']['average_speed']:.1f} km/h","Average speed of the athlete"],
        ["Maximum Burst Speed", f"{metrics['speed']['peak_speed']:.1f} km/h","Highest speed of the athlete"],
        ["Speed Consistency", f"{metrics['speed']['speed_consistency']:.1f}%","Depicts athlete consistency"],
        ["Average Heart Rate", f"{metrics['heart_rate']['average_hr']} bpm","Average heart rate of athlete"],
        ["Heart Rate Range", f"{metrics['heart_rate']['hr_range']} bpm","Range of heart rate"],
    ]
    
    movement_table = Table(movement_data, colWidths=[2*inch, 1.75*inch, 3.25*inch])
    movement_table = add_colored_table_style(movement_table, movement_data)
    story.append(movement_table)
    story.append(Spacer(1, 10))


    story.append(Paragraph("Detailed Performance Metrics", section_title_style))
    
    endurance_metrics = [
        ["Endurance Metrics", "Score", "Optimal Zone"],
        ["HRRI", f"{metrics['heart_rate']['hrri']} min",
         "Higher the better"],
        ["Fatigue Intensity", f"{metrics['fatigue']['fatigue_intensity']}",
         "8-10"],
        ["recovery rate", f"{metrics['heart_rate']['recovery_rate']} min",
         "Lower the better"],
    ]
    endurance_table = Table(endurance_metrics, colWidths=[1.75*inch, 1.5*inch, 1.75*inch, 2*inch])
    endurance_table = add_colored_table_style(endurance_table, endurance_metrics)
    story.append(endurance_table)

    
    return story

def get_assessment_level(score):
    """Returns assessment level data with color coding"""
    if score >= 8.5:
        return {
            'level': 'Excellent Performance',
            'color': '#27AE60',
            'percentage': score
        }
    elif score >= 7:
        return {
            'level': 'Advance Level',
            'color': '#2E86C1',
            'percentage': score
        }
    elif score >= 5:
        return {
            'level': 'Moderate Level',
            'color': '#F39C12',
            'percentage': score
        }
    else:
        return {
            'level': 'Devloping',
            'color': '#E74C3C',
            'percentage': score
        }

def get_rating(score):
    """Returns a rating based on score"""
    if score >= 90:
        return "★★★★★ Excellent"
    elif score >= 75:
        return "★★★★ Good"
    elif score >= 60:
        return "★★★ Average"
    elif score >= 40:
        return "★★ Fair"
    else:
        return "★ Needs Work"

def create_level_indicator(percentage):
    """Creates a visual level indicator"""
    return f"""
    <table width="100%" cellpadding="0" cellspacing="0">
        <tr>
            <td width="{percentage}%" bgcolor="#2E4053" height="20"></td>
            <td width="{100-percentage}%" bgcolor="#D5D8DC" height="20"></td>
        </tr>
        <tr>
            <td colspan="2" align="center">
                <font size="8" color="#7F8C8D">{percentage}% Complete</font>
            </td>
        </tr>
    </table>
    """
def create_achievement_indicator(value, min_target, max_target, higher_better=False):
    """Creates a visual achievement indicator"""
    if higher_better:
        if value >= max_target:
            return "★★★ Excellent"
        elif value >= min_target:
            return "★★ Good"
        else:
            return "★ Developing"
    else:
        if min_target <= value <= max_target:
            return "★★★ Optimal"
        elif value < min_target:
            return "★ Below Target"
        else:
            return "★ Above Target"

def create_heart_status(value, min_target, max_target, higher_better=False):
    """Creates heart rate status indicator"""
    if higher_better:
        if value >= max_target:
            return "✓ Excellent"
        elif value >= min_target:
            return "≈ Good"
        else:
            return "! Monitor"
    else:
        if min_target <= value <= max_target:
            return "✓ Optimal"
        else:
            return "! Monitor"



def get_endurance_assessment(fatigue_metrics):
    """Provides a detailed endurance assessment"""
    score = fatigue_metrics['endurance_score']
    maintenance = fatigue_metrics['speed_maintenance']
    hr_control = fatigue_metrics['hr_control']
    get_performance_level
    if score >= 90 and maintenance >= 90 and hr_control >= 90:
        return "Elite Level Endurance"
    elif score >= 75 and maintenance >= 75 and hr_control >= 75:
        return "Advanced Endurance Capacity"
    elif score >= 60 and maintenance >= 60 and hr_control >= 60:
        return "Intermediate Endurance Level"
    else:
        return "Developing Endurance Base"


def create_conclusion_page(story, styles, results):
    """Creates the conclusion page for cardiovascular assessment report"""
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
    
    story.append(PageBreak())
    metrics = calculate_performance_metrics(results)
    
    def get_performance_summary(metrics):
        # Calculate overall performance level based on key metrics
        endurance_score = metrics['fatigue']['endurance_score']
        hr_control = metrics['fatigue']['hr_control_score']
        speed_consistency = metrics['speed']['speed_consistency']
        overall_score = (endurance_score + hr_control + speed_consistency) / 3
        
        if overall_score >= 85:
            level = "elite"
            potential = "exceptional cardiovascular fitness suitable for high-performance athletics"
        elif overall_score >= 75:
            level = "good"
            potential = "strong cardiovascular base with excellent athletic potential"
        elif overall_score >= 55:
            level = "moderate"
            potential = "good foundation for cardiovascular development"
        else:
            level = "weak"
            potential = "foundational cardiovascular fitness requiring focused development"
            
        return level, potential, overall_score
    
    # Title Style
    title_style = ParagraphStyle(
        'ConclusionTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Create decorative top banner
    banner_table = Table([['Assessment Conclusion']], colWidths=[7.5*inch], rowHeights=[40])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 16),
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 20))
    
    # Get performance summary
    level, potential, overall_score = get_performance_summary(metrics)
    
    # Key Metrics Summary Box
    metrics_style = ParagraphStyle(
        'MetricsSummary',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    metrics_data = [
        [Paragraph(f"<b>Overall Fitness Score</b><br/>{overall_score:.1f}%", metrics_style),
         Paragraph(f"<b>Endurance Rating</b><br/>{metrics['fatigue']['endurance_score']:.1f}%", metrics_style),
         Paragraph(f"<b>Heart Rate Control</b><br/>{metrics['fatigue']['hr_control_score']:.1f}%", metrics_style),
         Paragraph(f"<b>Movement Efficiency</b><br/>{metrics['speed']['speed_consistency']:.1f}%", metrics_style)]
    ]
    
    metrics_table = Table(metrics_data, colWidths=[1.875*inch]*4)
    metrics_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 15),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 30))
    
    # Conclusion Text
    conclusion_style = ParagraphStyle(
        'Conclusion',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#2E4053')
    )
    
    conclusion_text = f"""Based on your cardiovascular assessment, you have demonstrated a <b>{level}</b> level of cardiovascular fitness, 
    indicating {potential}. Your performance shows particular strengths in {get_key_strength(metrics)} while 
    {get_improvement_area(metrics)}.
    
    This comprehensive analysis provides valuable insights into your cardiovascular capabilities, which are crucial for athletic performance 
    and overall fitness. By following the personalized training recommendations provided in this report, you can further enhance these 
    abilities and optimize your endurance potential."""
    
    story.append(Paragraph(conclusion_text, conclusion_style))
    story.append(Spacer(1, 30))
    
    # Key Takeaways Box
    takeaways_header = Table(
        [["KEY PERFORMANCE INSIGHTS"]], 
        colWidths=[7.5*inch],
        rowHeights=[30]
    )
    takeaways_header.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#34495E')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))
    story.append(takeaways_header)
    
    takeaways_style = ParagraphStyle(
        'Takeaways',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Generate personalized takeaways based on metrics
    takeaways_text = f"""
    • <b>Endurance Capacity:</b> {get_endurance_insight(metrics['fatigue']['endurance_score'])}
    
    • <b>Heart Rate Control:</b> {get_hr_control_insight(metrics['fatigue']['hr_control_score'])}
    
    • <b>Movement Efficiency:</b> {get_movement_insight(metrics['speed']['speed_consistency'])}
    
    • <b>Recovery Profile:</b> {get_recovery_insight(metrics['heart_rate'])}
    """
    
    takeaways_table = Table(
        [[Paragraph(takeaways_text, takeaways_style)]],
        colWidths=[7.5*inch]
    )
    takeaways_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('PADDING', (0, 0), (-1, -1), 15),
    ]))
    story.append(takeaways_table)
    story.append(Spacer(1, 30))
    
    # End Note
    endnote_style = ParagraphStyle(
        'EndNote',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    endnote_text = """Your cardiovascular fitness is a fundamental pillar of athletic performance. 
    Consistent training, proper recovery, and adherence to the recommended protocols will help you achieve your fitness goals.
    
    <b>Best wishes for your journey to excellence with Hyperlab. Your journey to peak performance continues!</b>"""
    
    story.append(Paragraph(endnote_text, endnote_style))
    
    # Decorative bottom banner
    story.append(Spacer(1, 30))
    bottom_banner = Table([['']], colWidths=[7.5*inch], rowHeights=[3])
    bottom_banner.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
    ]))
    story.append(bottom_banner)
    
    return story

def get_key_strength(metrics):
    """Determines the athlete's key strength"""
    scores = {
        'endurance': metrics['fatigue']['endurance_score'],
        'heart_rate': metrics['fatigue']['hr_control_score'],
        'movement': metrics['speed']['speed_consistency']
    }
    
    max_score = max(scores.items(), key=lambda x: x[1])
    
    strengths = {
        'endurance': 'maintaining consistent performance over extended periods',
        'heart_rate': 'excellent cardiovascular control and recovery',
        'movement': 'maintaining efficient movement patterns'
    }
    
    return strengths[max_score[0]]

def get_improvement_area(metrics):
    """Determines the primary area for improvement"""
    scores = {
        'endurance': metrics['fatigue']['endurance_score'],
        'heart_rate': metrics['fatigue']['hr_control_score'],
        'movement': metrics['speed']['speed_consistency']
    }
    
    min_score = min(scores.items(), key=lambda x: x[1])
    
    improvements = {
        'endurance': 'showing potential for enhanced endurance development',
        'heart_rate': 'indicating room for improved cardiovascular efficiency',
        'movement': 'presenting opportunities for movement pattern refinement'
    }
    
    return improvements[min_score[0]]

def get_endurance_insight(score):
    if score >= 85:
        return f"Exceptional endurance level ({score:.1f}%) - Capable of maintaining high performance over extended periods"
    elif score >= 70:
        return f"Strong endurance base ({score:.1f}%) - Good capacity for sustained activity with room for elite-level development"
    elif score >= 55:
        return f"Moderate endurance ({score:.1f}%) - Showing promise with clear potential for improvement"
    else:
        return f"Weak endurance foundation ({score:.1f}%) - Focus on progressive endurance training"

def get_hr_control_insight(score):
    if score >= 85:
        return f"Elite heart rate control ({score:.1f}%) - Excellent cardiovascular efficiency and recovery"
    elif score >= 70:
        return f"Advanced regulation ({score:.1f}%) - Good heart rate response with room for optimization"
    elif score >= 55:
        return f"Steady control ({score:.1f}%) - Developing cardiovascular adaptation"
    else:
        return f"Basic control ({score:.1f}%) - Priority area for cardiovascular development"

def get_movement_insight(score):
    if score >= 85:
        return f"Superior movement efficiency ({score:.1f}%) - Excellent speed consistency and control"
    elif score >= 70:
        return f"Good movement patterns ({score:.1f}%) - Stable performance with room for refinement"
    elif score >= 55:
        return f"Consistent movement ({score:.1f}%) - Developing pattern stability"
    else:
        return f"Basic movement control ({score:.1f}%) - Focus on movement quality and consistency"

def get_recovery_insight(hr_metrics):
    avg_hr = hr_metrics['average_hr']
    if avg_hr <= 140:
        return "Excellent recovery capacity - Efficient cardiovascular response to exercise"
    elif avg_hr <= 160:
        return "Good recovery profile - Effective heart rate regulation during activity"
    elif avg_hr <= 180:
        return "Moderate recovery - Shows potential for improved cardiovascular efficiency"
    else:
        return "Weak recovery - Focus on building cardiovascular efficiency"

def create_final_branding_page(story, styles):
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.platypus import Spacer, Table, TableStyle, Image
    story.append(PageBreak())
    story.append(Spacer(1, 2*inch))
    
    # Large centered logo
    logo_table = Table([[Image('hyperlab_logo.png', width=3*inch, height=1.2*inch)]], 
                      colWidths=[7.5*inch])
    logo_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(logo_table)
    
    story.append(Spacer(1, inch))
    
    # Company information
    info_style = ParagraphStyle(
        'CompanyInfo',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053'),
        spaceAfter=12
    )
    
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#5D6D7E'),
        spaceAfter=8
    )
    
    info_data = [
        [Paragraph("<b>HyperLab Sportech Pvt. Ltd.</b>", info_style)],
        [Paragraph("Advanced Performance Assessment & Training Solutions", contact_style)],
        [Paragraph("https://www.hyperlab.life/ | contact@hyperlab.life", contact_style)],
        [Paragraph("support@hyperlab.life", contact_style)],
    ]
    
    info_table = Table(info_data, colWidths=[7.5*inch])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(info_table)
    
    story.append(Spacer(1, 2*inch))
    
    # Bottom decorative element
    footer_text = "Excellence in Sports Science & Technology"
    footer_style = ParagraphStyle(
        'BrandingFooter',
        parent=styles['Normal'],
        fontSize=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E4053')
    )
    
    story.append(Paragraph(footer_text, footer_style))
    
    # Add decorative line
    line_table = Table([['']], colWidths=[5*inch], rowHeights=[1])
    line_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053'))
    ]))
    story.append(line_table)
    
    return story

def create_cardio_report(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by,results):
    doc = SimpleDocTemplate(
        f"cardiovascular_drill_report_{student_name.lower().replace(' ', '_')}.pdf",
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    # Create template with footer
    # create_report_template(doc)
    
    story = []
    styles = getSampleStyleSheet()
    story=create_first_page(student_name, device_used, assessment_date, drill_type, 
                     test_duration, assessed_by,story,styles)
    story=create_metrics_page(story,styles,results)
    # story=create_performance_metrics_page(story,styles,results)
    story=create_score_understanding_page(story,styles,results)
    metrics=calculate_performance_metrics(results)
    story=create_recommendations_page(story,styles,metrics)
    story=create_conclusion_page(story,styles,results)
    story = create_final_branding_page(story, styles)

    doc.build(story)
    return f"cardiovascular_drill_report_{student_name.lower().replace(' ', '_')}.pdf"

# Example usage
if __name__ == "__main__":
    # Sample athlete data
    report_file = create_cardio_report(
        student_name="Alex Thompson",
        device_used="HELIOS Pro v2.0",
        assessment_date="October 25, 2024",
        drill_type="Concentration Assessment",
        test_duration="5 minutes",
        assessed_by="Dr. Sarah Johnson",
        results={
        "msgtype": "cardiovascular_health",
        "speeds": [4.5, 5.2, 4.8, 5.0, 4.9, 5.1, 4.7, 5.3, 5.0, 4.9],
        "speedTimes": [1.2, 2.4, 3.7, 5.1, 6.4, 7.8, 9.2, 10.5, 11.9, 13.3],
        "highSpeed": 5.5,
        "lowSpeed": 4.5,
        "avgSpeed": 5.0,
        'heartrate':[172,180,191,190,191,192,180,200,201,202],
        'timestamp':[1,2,3,4,5,6,7,8,9,10],
        'heartrate_after90':205}
        
    )

    import os
    os.startfile(report_file)
    print(f"Report generated: {report_file}")