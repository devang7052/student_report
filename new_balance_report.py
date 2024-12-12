from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image,PageBreak
    # Calculate average metrics

def create_recommendations_section(story, right_metrics, left_metrics, styles):
    avg_success_rate = (right_metrics['hits_success_rate'] + left_metrics['hits_success_rate']) / 2
    avg_consistency = (right_metrics['balance_consistency'] + left_metrics['balance_consistency']) / 2
    symmetry_score = 1 - (abs(right_metrics['successful_hits'] - left_metrics['successful_hits']) / 20)
    avg_fatigue = (right_metrics['fatigue_resistance'] + left_metrics['fatigue_resistance']) / 2
    
    # Create title
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        textColor=colors.HexColor('#2E4053')
    )
    
    story.append(PageBreak())
    story.append(Paragraph("Personalized Recommendations", title_style))
    
    # Introduction paragraph
    intro_style = ParagraphStyle(
        'Intro',
        parent=styles['Normal'],
        fontSize=12,
        leading=14,
        spaceBefore=10,
        spaceAfter=20
    )
    
    story.append(Paragraph(
        "Based on your performance metrics, we've prepared personalized recommendations to help you improve your balance and stability. "
        "Focus on these exercises and gradually increase difficulty as you progress.",
        intro_style
    ))
    
    def create_recommendation_box(title, metric_value, ranges, recommendations):
        # Determine which recommendation to use based on metric value
        recommendation_text = ""
        metric_level = ""
        box_color = ""
        
        if title == "Success Rate":
            if metric_value >= 0.85:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 0.85>metric_value >= 0.7:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            elif 0.7>metric_value >= 0.5:
                recommendation_text = recommendations[2]
                metric_level = "Moderate"
                box_color = "#E67E22"
            else:
                recommendation_text = recommendations[3]
                metric_level = "Needs Improvement"
                box_color = "#E74C3C"
        
        elif title == "Balance Consistency":
            if metric_value <= 0.15:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 0.15<metric_value <= 0.3:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Needs Improvement"
                box_color = "#E74C3C"
        
        elif title == "Symmetry":
            if metric_value >= 0.9:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 0.9>metric_value >= 0.7:
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Needs Improvement"
                box_color = "#E74C3C"

        elif title == "Fatigue Resistance":
            if 1.1>=metric_value >= 0.9:
                recommendation_text = recommendations[0]
                metric_level = "Excellent"
                box_color = "#27AE60"
            elif 0.9>=metric_value >= 0.7 or 1.3>=metric_value >= 1.1 :
                recommendation_text = recommendations[1]
                metric_level = "Good"
                box_color = "#F39C12"
            else:
                recommendation_text = recommendations[2]
                metric_level = "Needs Improvement"
                box_color = "#E74C3C"
        
        # Create recommendation box
        reco_style = ParagraphStyle(
        'reco style',
        parent=styles['Normal'],
        alignment=4
    )
        box_data = [
            [Table(
                [[Paragraph(f"{title} Recommendations", styles['Heading3'])]],
                colWidths=[6*inch],
                style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(box_color)),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )],
            [Table(
                [[
                    Paragraph(f"Current Level: {metric_level}", styles['Normal']),
                    Paragraph(f"Score: {metric_value:.2f}", styles['Normal'])
                ]],
                colWidths=[3*inch, 3*inch],
                style=TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )],
            [Paragraph(recommendation_text, reco_style)]
        ]
        
        main_box = Table(
            box_data,
            colWidths=[6*inch],
            style=TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.grey),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFFFFF')),
                ('PADDING', (0, 0), (-1, -1), 10),
            ])
        )
        
        story.append(main_box)
        story.append(Spacer(1, 20))
    
    # Success Rate Recommendations
    success_recommendations = [
        "Great work! To maintain this level, challenge yourself with advanced exercises like single-leg deadlifts, lateral hops, or dynamic lunges that test your balance while moving. You can also incorporate resistance band reaches to further develop stability and coordination.",
        "Good performance! Focus on improving consistency with exercises like step-ups on a box or bosu ball squats to work on your balance and control. Practicing yoga poses such as tree pose and warrior pose will also help in strengthening your balance.",
        "You're showing progress but need to build more stability. Incorporate core strengthening exercises like planks and bird dogs. Practicing balance board exercises or using a foam roller for stability training will help improve your control.",
        "Focus on foundational balance exercises. Start with heel-to-toe walks, single-leg stands, and wall-supported leg lifts. These will help you develop the muscle strength and coordination needed before advancing to more challenging activities."
    ]
    create_recommendation_box("Success Rate", avg_success_rate, [], success_recommendations)
    
    # Balance Consistency Recommendations
    consistency_recommendations = [
        "To maintain your excellent balance, incorporate exercises like single-leg squats or pistol squats to further challenge your stability. Try balance board activities that engage your core while improving your coordination.",
        "You have fairly consistent balance, but to further improve, work on bosu ball balance exercises or dynamic stability moves, like side lunges with knee raises. Adding Tai Chi to your routine can also help improve focus and coordination.",
        "Improve your consistency by incorporating slow walking lunges or cross-body reaches. Focus on core exercises like Russian twists and stability ball work to enhance control during longer or more challenging tasks."
    ]
    create_recommendation_box("Balance Consistency", avg_consistency, [], consistency_recommendations)
    
    # Fatigue Resistance Recommendations
    fatigue_recommendations = [
        "To continue building fatigue resistance, include endurance activities like cycling, swimming, or long-distance running into your routine. Also, add high-intensity interval training (HIIT) sessions that maintain balance under fatigue.",
        "Improve endurance with circuit training or exercises like jump rope and mountain climbers. These activities build stamina while improving balance. Incorporate bodyweight exercises to sustain balance even under fatigue.",
        "Build endurance through low-impact exercises like brisk walking, cycling, or elliptical training. Begin with shorter durations and gradually increase workout length. Combine endurance exercises with simple balance challenges such as single-leg stands."
    ]
    create_recommendation_box("Fatigue Resistance", avg_fatigue, [], fatigue_recommendations)
    
    # Symmetry Recommendations
    symmetry_recommendations = [
        "Your performance is well-balanced between both sides. Keep up the great work with bilateral exercises like walking lunges, side planks, or kettlebell swings that maintain even strength and coordination on both sides.",
        "Focus on improving the weaker side with unilateral exercises like single-leg squats, single-arm presses, or side leg raises. Add balance-focused yoga such as warrior poses to even out strength discrepancies.",
        "Work on building symmetry by practicing alternating lunges, single-leg bridges, and single-arm kettlebell rows. Balance-focused exercises like side leg raises or single-leg deadlifts can help target your weaker side."
    ]
    create_recommendation_box("Symmetry", symmetry_score, [], symmetry_recommendations)
    
    # Final note
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        leftIndent=20,
        rightIndent=20,
        spaceBefore=20,
        alignment=4
    )
    
    story.append(Paragraph(
        "<i>Note: These recommendations are based on your current performance levels. Always start with easier variations "
        "and progress gradually. Consult with your healthcare provider before starting any new exercise program. All the exercise mentioned above are available on web you can take reference from there.</i>",
        note_style
    ))

def create_conclusion(story, right_metrics, left_metrics, styles):
    # Calculate key metrics
    right_completion = right_metrics['completion_percentage']
    left_completion = left_metrics['completion_percentage']
    better_side = "right" if right_completion > left_completion else "left"
    avg_success_rate = (right_metrics['hits_success_rate'] + left_metrics['hits_success_rate']) / 2
    symmetry_score = 1 - (abs(right_metrics['successful_hits'] - left_metrics['successful_hits']) / 20)
    avg_consistency = (right_metrics['balance_consistency'] + left_metrics['balance_consistency']) / 2
    avg_fatigue = (right_metrics['fatigue_resistance'] + left_metrics['fatigue_resistance']) / 2

    story.append(PageBreak())
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        textColor=colors.HexColor('#2E4053')
    )
    story.append(Paragraph("Assessment Conclusion", title_style))
    
    # Overview box
    overview_style = ParagraphStyle(
        'Overview',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        spaceBefore=10,
        spaceAfter=10
    )

    def determine_overall_level(metrics):
        # Calculate average of normalized metrics
        normalized_success = (avg_success_rate)
        normalized_symmetry = (symmetry_score)
        normalized_consistency = (1 - avg_consistency)  # Inverse as lower is better
        normalized_fatigue = (avg_fatigue if avg_fatigue <= 1 else 2 - avg_fatigue)  # Adjust for optimal being 1.0
        
        avg_score = (normalized_success + normalized_symmetry + normalized_consistency + normalized_fatigue) / 4
        
        if avg_score >= 0.8:
            return "Advanced"
        elif avg_score >= 0.6:
            return "Intermediate"
        else:
            return "Beginner"

    overall_level = determine_overall_level([avg_success_rate, symmetry_score, avg_consistency, avg_fatigue])
    
    # Create the main conclusion box
    conclusion_data = [
        [Table(
            [[Paragraph("Performance Summary", styles['Heading3'])]],
            colWidths=[7*inch],
            style=TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('PADDING', (0, 0), (-1, -1), 8),
            ])
        )],
        [Paragraph(
            f"Overall Level: <b>{overall_level}</b><br/>"
            f"Dominant Side: <b>{better_side.capitalize()}</b><br/>"
            f"Assessment Date: <b>{datetime.now().strftime('%Y-%m-%d')}</b>",
            overview_style
        )],
    ]
    
    main_box = Table(
        conclusion_data,
        colWidths=[7*inch],
        style=TableStyle([
            ('BOX', (0, 0), (-1, -1), 1, colors.grey),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
            ('PADDING', (0, 0), (-1, -1), 10),
        ])
    )
    
    story.append(main_box)
    story.append(Spacer(1, 20))
    
    # Strengths and Areas for Improvement
    def create_analysis_box(title, content, box_color):
        box_data = [
            [Table(
                [[Paragraph(title, styles['Heading3'])]],
                colWidths=[7*inch],
                style=TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(box_color)),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )],
            [Paragraph(content, styles['Normal'])]
        ]
        
        return Table(
            box_data,
            colWidths=[7*inch],
            style=TableStyle([
                ('BOX', (0, 0), (-1, -1), 1, colors.grey),
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFFFFF')),
                ('PADDING', (0, 0), (-1, -1), 10),
            ])
        )
    
    # Determine strengths and areas for improvement
    strengths = []
    improvements = []
    
    if avg_success_rate >= 0.8:
        strengths.append("High success rate in target acquisition")
    elif avg_success_rate < 0.6:
        improvements.append("Target acquisition accuracy")
        
    if symmetry_score >= 0.8:
        strengths.append("Excellent balance symmetry between sides")
    elif symmetry_score < 0.6:
        improvements.append(f"Balance symmetry (particularly on the {('left' if better_side == 'right' else 'right')} side)")
        
    if avg_consistency <= 0.2:
        strengths.append("Consistent balance maintenance")
    elif avg_consistency > 0.5:
        improvements.append("Balance consistency")
        
    if 0.9 <= avg_fatigue <= 1.1:
        strengths.append("Strong fatigue resistance")
    elif avg_fatigue < 0.8 or avg_fatigue > 1.2:
        improvements.append("Fatigue resistance")
    
    # Create strength summary
    strengths_text = "• " + "\n• ".join(strengths) if strengths else "No significant strengths identified - continue working on all aspects of balance control."
    story.append(create_analysis_box("Key Strengths", strengths_text, "#27AE60"))
    story.append(Spacer(1, 20))
    
    # Create improvements summary
    improvements_text = "• " + "\n• ".join(improvements) if improvements else "No significant areas for improvement - maintain current performance levels."
    story.append(create_analysis_box("Areas for Improvement", improvements_text, "#E74C3C"))
    story.append(Spacer(1, 20))
    
    # Primary Focus Exercises
    def determine_primary_exercises():
        exercises = []
        
        # Add exercises based on metrics
        if avg_success_rate < 0.6:
            exercises.append("Basic balance exercises (heel-to-toe walks, single-leg stands)")
        elif avg_consistency > 0.5:
            exercises.append("Stability exercises (bosu ball work, balance board training)")
        
        if symmetry_score < 0.7:
            exercises.append(f"Unilateral exercises focusing on the {('left' if better_side == 'right' else 'right')} side")
        
        if avg_fatigue < 0.8:
            exercises.append("Endurance-focused exercises (circuit training, progressive duration activities)")
            
        # Add level-specific exercises
        if overall_level == "Beginner":
            exercises.append("Foundation exercises (wall-supported balance work, basic core strengthening)")
        elif overall_level == "Intermediate":
            exercises.append("Progressive challenges (dynamic balance exercises, stability ball work)")
        else:
            exercises.append("Advanced drills (complex movement patterns, reactive balance training)")
            
        return exercises
    
    primary_exercises = determine_primary_exercises()
    exercises_text = "Based on your assessment, focus on these key exercises:\n\n• " + "\n• ".join(primary_exercises)
    story.append(create_analysis_box("Recommended Focus Areas", exercises_text, "#2874A6"))
    story.append(Spacer(1, 20))
    
    # Final note
    note_style = ParagraphStyle(
        'Note',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#2E4053'),
        leftIndent=20,
        rightIndent=20,
        spaceBefore=20
    )
    
    story.append(Paragraph(
        "<b>Next Steps:</b> Schedule a follow-up assessment in 4-6 weeks to track your progress. "
        "Focus on the recommended exercises while maintaining proper form and gradually increasing difficulty. "
        f"Your {better_side} side shows stronger performance - use this as a reference point while working to improve "
        f"the {('left' if better_side == 'right' else 'right')} side. Remember to always warm up properly and listen to your body during training.",
        note_style
    ))  
    return story
def create_first_page(story, styles):
    # Custom styles for better presentation
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
    
    story.append(Spacer(1, 10))

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        alignment=1,  # Center alignment
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
        firstLineIndent=0,
        alignment=4  # Justified alignment
    )
    
    highlight_text_style = ParagraphStyle(
        'HighlightText',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#2E4053'),
        backColor=colors.HexColor('#F8F9F9'),
        borderPadding=5
    )

    # Title
    story.append(Paragraph("Balance Drill Performance Report", title_style))
    
    # Information table
    current_date = datetime.now().strftime("%Y-%m-%d")
    info_data = [
        ["Student Name:", student_name, "Date of Assessment:", current_date],
        ["Device Used:", "HELIOS", "Drill Type:", "Dynamic Balance Drill"],
        ["Test Duration:", "20 minutes", "Assessed by:", instructor_name]
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
    story.append(Spacer(1, 10))

    # Introduction Section
    story.append(Paragraph("Introduction", section_title_style))
    
    # Enhanced introduction paragraphs
    intro_text = "The <b>Balance Drill</b> is designed to assess a student's <b>postural control</b> and <b>dynamic balance</b> using the advanced <b>HELIOS device</b>. This drill challenges participants to stand on one leg and reach for targets at various positions, testing their ability to stabilize the body while reacting to changing stimuli."
    story.append(Paragraph(intro_text, intro_paragraph_style))
    
    story.append(Spacer(1, 1))
    
    intro_text2 = "The drill's primary objective is to measure <b>balance proficiency</b>, focusing on both <b>equilibrium maintenance</b> and <b>reactive control</b>. By analyzing how students respond to shifts in target locations, the drill provides valuable insights into their body awareness and stability. The HELIOS device offers <b>real-time feedback</b>, ensuring accurate and standardized assessments for each individual, while gradually increasing the difficulty level to further challenge their balance capabilities."
    story.append(Paragraph(intro_text2, intro_paragraph_style))
    
    story.append(Spacer(1, 1))

    story.append(Paragraph("Procedure", section_title_style))
    
    # Step-by-Step Procedure Box
    procedure_data = [
        ["Step", "Description", "Scoring"],
        ["1. Setup", "Square boundary projection\nSingle-leg stance", ""],
        ["2. Initiation", "Tap trail point to begin", ""],
        ["3. Execution", "20 targets per side\nTimed responses", "Success = 1 point\nBalance break = 0 points"],
        ["4. Reset", "Switches leg after 1 miss", ""],
        ["5. Completion", "Complete all targets or\nReach maximum misses", "Final score calculation"]
    ]
    
    procedure_table = Table(procedure_data, colWidths=[1.5*inch, 2.5*inch, 2*inch])
    procedure_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#E8E8E8')),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F4F6F7')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    
    story.append(procedure_table)
    
    # Footer note
    # footer_style = ParagraphStyle(
    #     'Footer',
    #     parent=styles['Normal'],
    #     fontSize=8,
    #     textColor=colors.HexColor('#666666'),
    #     alignment=1,
    #     spaceBefore=1
    # )
    
    # story.append(Spacer(1, 2))
    # story.append(Paragraph(
    #     "<i>This assessment provides a standardized evaluation of balance capabilities "
    #     "using the HELIOS device. Results are used to track progress and identify areas "
    #     "for improvement in balance control and stability.</i>",
    #     footer_style
    # ))
    return story

def calculate_metrics(scores, total_targets=20):
    successful_hits = sum(scores)
    balance_breaks = len(scores) - successful_hits
    misses = total_targets - len(scores)
    completion_status = "Completed Sucessfully" if len(scores) == total_targets else f"Unsucessfull"
    hits_success_rate = successful_hits / total_targets
    
    # Calculate new metrics
    balance_consistency = balance_breaks / len(scores) if len(scores) > 0 else 0
    
    # Calculate fatigue resistance

    first_five = sum(scores[:5]) if len(scores) >= 5 else sum(scores)
    last_five = sum(scores[-5:]) if len(scores) >= 5 else sum(scores)
    fatigue_resistance = first_five / last_five if last_five > 0 else 0
    
    completion_percentage = successful_hits / total_targets
    
    return {
        'successful_hits': successful_hits,
        'balance_breaks': balance_breaks,
        'misses': misses,
        'completion_status': completion_status,
        'hits_success_rate': hits_success_rate,
        'completion_percentage': completion_percentage,
        'balance_consistency': balance_consistency,
        'fatigue_resistance': fatigue_resistance
    }

def create_final_branding_page(story, styles):
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from reportlab.platypus import Spacer, Table, TableStyle, Image
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

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

def create_conclusion_section(story, right_metrics, left_metrics, styles):
    # Calculate overall metrics for assessment
    total_score = (right_metrics['completion_percentage'] + left_metrics['completion_percentage']) / 2
    symmetry_score = 1 - (abs(right_metrics['successful_hits'] - left_metrics['successful_hits']) / 20)
    avg_consistency = (right_metrics['balance_consistency'] + left_metrics['balance_consistency']) / 2
    avg_fatigue = (right_metrics['fatigue_resistance'] + left_metrics['fatigue_resistance']) / 2
    
    # Create custom styles for conclusion section
    title_style = ParagraphStyle(
        'ConclusionTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        textColor=colors.HexColor('#2E4053')
    )
    
    subtitle_style = ParagraphStyle(
        'ConclusionSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor('#2E4053')
    )
    
    content_style = ParagraphStyle(
        'ConclusionContent',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceBefore=5,
        spaceAfter=10,
        alignment=4
    )
    
    # Add main title
    story.append(Paragraph("Assessment Conclusion", title_style))
    
    # # Overall Assessment Section
    # story.append(Paragraph("Overall Assessment", subtitle_style))
    
    # Generate appropriate assessment text based on metrics
    performance_level = "excellent" if total_score > 0.85 else "good" if total_score > 0.7 else "developing"
    consistency_level = "high" if avg_consistency < 0.15 else "moderate" if avg_consistency < 0.3 else "variable"
    fatigue_impact = (
        "maintained consistent performance" if 0.9 <= avg_fatigue <= 1.1
        else "showed some fatigue effects" if 0.8 <= avg_fatigue <= 1.2
        else "demonstrated significant performance changes"
    )
    symmetry_description = (
        "excellent balance symmetry" if symmetry_score > 0.9
        else "good symmetry with minor differences" if symmetry_score > 0.7
        else "notable asymmetry"
    )
    
    overall_assessment = f"""
    The assessment reveals {performance_level} balance control capabilities with an overall success rate of {total_score:.1%}. 
    Throughout the drill, you demonstrated {consistency_level} stability maintenance and {fatigue_impact} as the assessment 
    progressed. Your performance showed {symmetry_description} between right and left sides, suggesting 
    {
        'well-developed bilateral control' if symmetry_score > 0.9
        else 'generally balanced bilateral development with room for refinement' if symmetry_score > 0.7
        else 'an opportunity for improving balance equality between sides'
    }.

    <b>Best wishes for your journey to excellence with Hyperlab. Your journey to peak performance continues!</b>
    """
    
    story.append(Paragraph(overall_assessment, content_style))
    
    # Next Steps Section
    story.append(Spacer(1, 13))
    story.append(Paragraph("Personalized Development Plan", title_style))
    story.append(Spacer(1, 5))
    
    # Create tables for each phase of training
    def create_phase_table(phase_title, exercises, duration, frequency):
        data = [
            [Paragraph(f"<b>{phase_title}</b>", styles['Normal']), 
             Paragraph(f"<b>Duration:</b> {duration}", styles['Normal']),
             Paragraph(f"<b>Frequency:</b> {frequency}", styles['Normal'])],
            [Paragraph("<b>Exercise</b>", styles['Normal']),
             Paragraph("<b>Sets × Reps</b>", styles['Normal']),
             Paragraph("<b>Progression</b>", styles['Normal'])]
        ]
        
        for exercise in exercises:
            data.append([
                Paragraph(exercise[0], styles['Normal']),
                Paragraph(exercise[1], styles['Normal']),
                Paragraph(exercise[2], styles['Normal'])
            ])
        
        table = Table(data, colWidths=[3*inch, 1.5*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EBF5FB')),
            ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#2E4053')),
            ('TEXTCOLOR', (0, 1), (-1, 1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('FONTNAME', (0, 0), (-1, 1), 'Helvetica-Bold'),
        ]))
        return table

    # Define exercise programs based on performance
    if total_score < 0.7:
        # Foundational Program
        phase1_exercises = [
            ("Single-Leg Balance Hold", "3 × 30s each", "Add arm movements"),
            ("Tandem Stance Walking", "3 × 20 steps", "Decrease base width"),
            ("Bird Dog Exercise", "3 × 10 each side", "Increase hold time")
        ]
        
        phase2_exercises = [
            ("BOSU Ball Balance", "3 × 45s each side", "Close eyes"),
            ("Step-Up with Hold", "3 × 12 each leg", "Add weights"),
            ("Walking Lunges", "3 × 16 steps", "Add dynamic arms")
        ]
        
        phase3_exercises = [
            ("Single-Leg Reach", "3 × 10 each", "Increase reach distance"),
            ("Balance Disc Squats", "3 × 15", "Add pulses at bottom"),
            ("Dynamic Step Touch", "3 × 30s", "Increase speed")
        ]
    
    elif total_score < 0.85:
        # Intermediate Program
        phase1_exercises = [
            ("BOSU Ball Single-Leg Hold", "4 × 45s each", "Add head movements"),
            ("Walking Heel-to-Toe", "4 × 30 steps", "Close eyes briefly"),
            ("Single-Leg Romanian Deadlift", "3 × 12 each", "Add weight")
        ]
        
        phase2_exercises = [
            ("Stability Ball Kneeling", "3 × 60s", "Add arm patterns"),
            ("Cross-Body Step-Ups", "4 × 15 each", "Increase step height"),
            ("Balance Board Circles", "3 × 45s each way", "Add ball toss")
        ]
        
        phase3_exercises = [
            ("Single-Leg Hop Stick", "3 × 10 each", "Add direction changes"),
            ("BOSU Burpees", "3 × 12", "Add push-up"),
            ("Star Balance Reach", "3 × 8 each leg", "Increase reach")
        ]
    
    else:
        # Advanced Program
        phase1_exercises = [
            ("Single-Leg BOSU Squat", "4 × 12 each", "Add perturbations"),
            ("Dynamic Balance Matrix", "3 × 45s", "Increase pattern complexity"),
            ("Suspended Single-Leg Pike", "3 × 10 each", "Add rotation")
        ]
        
        phase2_exercises = [
            ("Reactive Balance Drill", "4 × 30s each", "Add cognitive task"),
            ("Multi-Planar Lunge Matrix", "3 × 16 total", "Add power element"),
            ("Single-Leg Box Drill", "3 × 4 each way", "Increase speed")
        ]
        
        phase3_exercises = [
            ("Plyometric Balance Series", "3 × 45s", "Add combination moves"),
            ("Advanced Stability Flow", "3 × 60s", "Reduce rest time"),
            ("Agility Balance Complex", "3 × 30s each", "Add reaction drill")
        ]

    # Add tables to story
    story.append(create_phase_table("Phase 1: Foundation (Weeks 1-2)", 
                                  phase1_exercises, 
                                  "2 Weeks", 
                                  "3-4 sessions/week"))
    story.append(Spacer(1, 15))
    
    story.append(create_phase_table("Phase 2: Development (Weeks 3-4)", 
                                  phase2_exercises, 
                                  "2 Weeks", 
                                  "3-4 sessions/week"))
    story.append(Spacer(1, 15))
    
    story.append(create_phase_table("Phase 3: Advanced Integration (Weeks 5-6)", 
                                  phase3_exercises, 
                                  "2 Weeks", 
                                  "3-4 sessions/week"))
    
    # Important Notes Section
    story.append(Spacer(1, 20))
    notes_style = ParagraphStyle(
        'Notes',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#2E4053'),
        borderColor=colors.HexColor('#2E4053'),
        borderWidth=1,
        borderPadding=10,
        borderRadius=5
    )
    
    important_notes = """
    <b>Important Notes:</b>
    • All exercise are easily available on web take reference from there.
    • Always perform a proper warm-up before beginning these exercises
    • Start each session with the easier variations and progress as comfort allows
    • Maintain proper form throughout - quality over quantity
    • If you experience any pain or severe discomfort, stop and consult your instructor
    • Stay well-hydrated and wear appropriate footwear
    • Schedule a follow-up assessment after completing the 6-week program
    """
    
    story.append(Paragraph(important_notes, notes_style))


def create_balance_report(student_name, instructor_name, left_scores, right_scores):
    # Create the PDF document
    doc = SimpleDocTemplate(
        f"balance_report_{student_name.replace(' ', '_')}.pdf",
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Container for the 'Flowables'
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    story = create_first_page(story, styles)
    story.append(PageBreak())
    
    # Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=20,
        textColor=colors.HexColor('#2E4053')
    )
    
    # Calculate metrics
    right_metrics = calculate_metrics(right_scores)
    left_metrics = calculate_metrics(left_scores)

    # Summary of Results - Side by Side
    # story.append(Paragraph("3. Summary of Results", title_style))
    story.append(Paragraph("Performance Summary", title_style))

            # Helper function to get level data based on score
    def get_assessment_level(score):
        if score >= 8.5:
            return {
                'level': 'Excellent',
                'color': '#27AE60',
                'percentage': score * 10  # Convert to percentage
            }
        elif score >= 7:
            return {
                'level': 'Good',
                'color': '#F39C12',
                'percentage': score * 10
            }
        elif score >= 5:
            return {
                'level': 'Fair',
                'color': '#E67E22',
                'percentage': score * 10
            }
        else:
            return {
                'level': 'Devloping',
                'color': '#E74C3C',
                'percentage': score * 10
            }

        # Helper function to create level indicator bar

        # Get level data based on final score
    level_data = get_assessment_level((right_metrics['successful_hits']/2+left_metrics["successful_hits"]/2)/2)
    total_score = ( right_metrics['successful_hits']/2 + left_metrics['successful_hits']/2) / 2
    # Create assessment box with score
    assessment_content = [
        [Paragraph(f"""
            <font color='{level_data['color']}' size='11'><b>{level_data['level']}</b></font>
            <br/>
            <font color="#7F8C8D" size='8'><b>Overall Score: {total_score:.1f}/10</b></font>
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
    story.append(Spacer(1, 20))
    
    # Add descriptive text
    summary_intro = """The following summary presents a detailed breakdown of your performance across both sides. 
    The assessment evaluates multiple aspects of balance control, including target accuracy, balance maintenance, 
    and overall completion success."""
    story.append(Paragraph(summary_intro, styles['Normal']))
    story.append(Spacer(1, 20))

    summary_data = [
        ["Metrics", "Right Side", "Left Side"],
        ["Total Targets Attempted", "20", "20"],
        ["Successful Hits", str(right_metrics['successful_hits']), str(left_metrics['successful_hits'])],
        ["Balance Breaks", str(right_metrics['balance_breaks']), str(left_metrics['balance_breaks'])],
        ["Misses", str(right_metrics['misses']), str(left_metrics['misses'])],
        ["Completion Status", right_metrics['completion_status'], left_metrics['completion_status']]
    ]
    
    summary_table = Table(summary_data, colWidths=[2.5*inch, 2.5*inch, 2.5*inch])
    summary_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    
    story.append(summary_table)
    story.append(Spacer(1, 30))
    

    story.append(Paragraph("Detailed Performance Metrics", title_style))
    
    metrics_intro = """The following metrics provide a comprehensive analysis of your balance performance. 
    Each metric evaluates different aspects of balance control and movement efficiency."""
    story.append(Paragraph(metrics_intro, styles['Normal']))
    story.append(Spacer(1, 20))

    # Create enhanced metrics table with descriptions
    metrics_data = [
        ["Metric", "Right Side", "Left Side", "Description"],
        ["Balance Score", 
         f"{right_metrics['successful_hits']/2}/10", 
         f"{left_metrics['successful_hits']/2}/10", 
         "Raw score based on successful target hits"],
        ["Success Rate", 
         f"{right_metrics['hits_success_rate']:.1%}", 
         f"{left_metrics['hits_success_rate']:.1%}",
         "Percentage of successful hits relative to attempts"],
        ["Balance Consistency", 
         f"{right_metrics['balance_consistency']:.2f}", 
         f"{left_metrics['balance_consistency']:.2f}",
         "Measure of stability maintenance (lower is better)"],
        ["Fatigue Resistance", 
         f"{right_metrics['fatigue_resistance']:.2f}", 
         f"{left_metrics['fatigue_resistance']:.2f}",
         "Shows Performance consistency(should be near to 1)"],

        ["Completion %", 
         f"{right_metrics['completion_percentage']:.1%}", 
         f"{left_metrics['completion_percentage']:.1%}",
         "Overall task completion rate"]
    ]

    metrics_table = Table(metrics_data, colWidths=[1.5*inch, 1.25*inch, 1.25*inch, 3.5*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9F9')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#EBF5FB')),
    ]))

    story.append(metrics_table)
    story.append(Spacer(1, 30))

    total_score = ( right_metrics['successful_hits']/2 + left_metrics['successful_hits']/2) / 2
    symmetry_score = 1 - (abs(right_metrics['successful_hits'] - left_metrics['successful_hits']) / 20)
    
    performance_level = "Excellent" if total_score > 0.8 else "Good" if total_score > 0.6 else "Needs Improvement"
    performance_color = {
        "Excellent": "#27AE60",
        "Good": "#F39C12",
        "Needs Improvement": "#E74C3C"
    }[performance_level]
    
    overall_data = [
        ["Overall Performance Summary"],
        ["Total Score:", f"{total_score}"],
        ["Balance Symmetry:", f"{symmetry_score:.1%}"],
        ["Performance Level:", f"{performance_level}"],
        ["Dominant Side:", "Right" if right_metrics['completion_percentage'] > left_metrics['completion_percentage'] else "Left"]
    ]

    overall_table = Table(overall_data, colWidths=[1.75*inch, 1.75*inch])
    overall_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E4053')),
        ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#EBF5FB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('SPAN', (0, 0), (1, 0)),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('PADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 2, colors.HexColor('#2E4053')),
    ]))

    story.append(overall_table)
    # note_style = ParagraphStyle(
    #         'Note',
    #         parent=styles['Normal'],
    #         fontSize=9,
    #         textColor=colors.HexColor('#666666'),
    #         leftIndent=20,
    #         rightIndent=20,
    #         spaceBefore=20,
    #         alignment=4
    #     )
        
    # # Add quick interpretation
    # interpretation = f"""
 
    # <para><b>Quick Interpretation:</b> Your assessment shows a  {'bad' if performance_level.lower()=="needs improvement" else performance_level.lower()} level of balance control 
    # with an overall success rate of {total_score}. The symmetry score of {symmetry_score:.1%} indicates {'excellent symmetry between right and left sides' if symmetry_score > 0.9  else 'good symmetry between right and left sides' if 0.9>=symmetry_score >= 0.7  else 'some asymmetry between right and left sides.'},
    # {'Consider focusing on improving consistency across both sides.' if symmetry_score < 0.9 else ''}</para>
    # """
    # story.append(Spacer(1, 20))
    # story.append(Paragraph(interpretation, note_style))
    story.append(PageBreak())
    def create_interpretation_section(story, right_metrics, left_metrics):
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            textColor=colors.HexColor('#2E4053')
        )
        
        story.append(Paragraph("Understanding Your Scores", title_style))
        
        # Calculate overall metrics
        total_score = (right_metrics['completion_percentage']/2 + left_metrics['completion_percentage']/2) / 2
        symmetry_score = 1 - (abs(right_metrics['successful_hits'] - left_metrics['successful_hits']) / 20)
        
        def get_performance_level(score, metric_type):
            if metric_type == "completion":
                return "Excellent" if score > 0.85 else "Good" if score > 0.70 else "Needs Improvement"
            elif metric_type == "consistency":
                return "Excellent" if score < 0.15 else "Good" if score < 0.30 else "Needs Improvement"
            elif metric_type == "fatigue":
                return "Excellent" if 0.9 <= score <= 1.1 else "Good" if 0.8 <= score <= 1.2 else "Needs Improvement"
            elif metric_type == "symmetry":
                return "Excellent" if score > 0.9 else "Good" if score > 0.7 else "Needs Improvement"
            
        def create_metric_box(title, score, score_type, what_is,calculation, interpretation,optimal_range, recommendations,calc=''):
            # Create container table
            main_table_data = [[
                Table(
                    [[Paragraph(f"<b>{title}</b>", styles['Heading3'])]],
                    colWidths=[4*inch],
                    style=TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#2E4053')),
                        ('TEXTCOLOR', (0, 0), (-1, -1), colors.white),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('PADDING', (0, 0), (-1, -1), 8),
                    ])
                )
            ]]
            
            # Performance level and score
            level = get_performance_level(score, score_type)
            level_color = {
                "Excellent": "#27AE60",
                "Good": "#F39C12",
                "Needs Improvement": "#E74C3C"
            }[level]
            
            score_table = Table(
                [[
                    Paragraph(f"Your Score:", styles['Normal']),
                    Paragraph(f"<b>{score:.2f}</b>", styles['Normal']),
                    Paragraph(f"<font color='{level_color}'>{level}</font>", styles['Normal'])
                ]],
                colWidths=[1.5*inch, 1*inch, 1.5*inch],
                style=TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8F9F9')),
                    ('PADDING', (0, 0), (-1, -1), 8),
                ])
            )
            main_table_data.append([score_table])
            
            # Content sections
            content_style = ParagraphStyle(
                'Content',
                parent=styles['Normal'],
                fontSize=10,
                leading=14,
                spaceBefore=5,
                spaceAfter=5,
                alignment=4
            )
            
            content_data = [
                [Paragraph("<b>What is it?</b>", content_style)],
                [Paragraph(what_is, content_style)],
                [Paragraph("<b>How it's calculated:</b>", content_style)],
                [Paragraph(calc, content_style)],
                [Paragraph(calculation, content_style)],
                [Paragraph("<b>Your Performance:</b>", content_style)],
                [Paragraph(interpretation, content_style)],
                [Paragraph(optimal_range, content_style)],
                [Paragraph("<b>Inference:</b>", content_style)],
                [Paragraph(recommendations, content_style)]
            ]
            
            content_table = Table(
                content_data,
                colWidths=[6*inch],
                style=TableStyle([
                    ('PADDING', (0, 0), (-1, -1), 6),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFFFFF')),
                ])
            )
            main_table_data.append([content_table])
            
            # Create main container
            main_table = Table(
                main_table_data,
                colWidths=[6*inch],
                style=TableStyle([
                    ('BOX', (0, 0), (-1, -1), 1, colors.grey),
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F4F6F7')),
                    ('PADDING', (0, 0), (-1, -1), 10),
                ])
            )
            
            story.append(main_table)
            story.append(Spacer(1, 20))
        
        # Completion Percentage
        right_completion = right_metrics['completion_percentage']
        left_completion = left_metrics['completion_percentage']
        avg_completion = ((right_completion + left_completion) / 2)
        
        create_metric_box(
            "Drill Completion ability",
            avg_completion,
            "completion",
            "A measure of your success rate in hitting targets while maintaining balance.",
            f"Right Side: {right_completion:.1%} | Left Side: {left_completion:.1%} | Average: {avg_completion:.1%}",
            f"You successfully completed {avg_completion:.1%} of targets across both sides. ",
            f'Optimal Range: Excellent: >85% | Good: 70-85% | Needs Improvement: <70%',
            " This score directly reflects your ability to maintain balance while reaching targets. A higher percentage indicates better overall performance and control during the assessment.",
            f"Calculated as: (Number of Successful Hits ÷ Total Targets) × 100",
            
        )
        
        # Balance Consistency Index
        right_bci = right_metrics['balance_consistency']
        left_bci = left_metrics['balance_consistency']
        avg_bci = (right_bci + left_bci) / 2
        
        create_metric_box(
            "Balance Consistency Index (BCI)",
            avg_bci,
            "consistency",
            "Measures how well you maintain balance throughout the assessment.",
            f"Right Side: {right_bci:.2f} | Left Side: {left_bci:.2f} | Average: {avg_bci:.2f}",
            f"Your BCI of {avg_bci:.2f} indicates " + (
                "excellent balance control with minimal disruptions." if avg_bci < 0.15 else
                "good balance control with occasional disruptions." if avg_bci < 0.30 else
                "frequent balance disruptions that need attention."
            ),
            f'Optimal Range:Excellent: <0.15 | Good: 0.15-0.30 | Needs Improvement: >0.3',

            "A lower BCI indicates better balance control. Each balance break represents a moment where control was lost, so fewer breaks (lower index) suggests better postural control and stability.",
            'Calculated as: Number of Balance Breaks/Total Attempts',
        )
        story.append(PageBreak())
        
        # Fatigue Resistance
        right_fr = right_metrics['fatigue_resistance']
        left_fr = left_metrics['fatigue_resistance']
        avg_fr = (right_fr + left_fr) / 2
        
        create_metric_box(
            "Fatigue Resistance",
            avg_fr,
            "fatigue",
            "Shows how well you maintain performance from start to finish.",
            f"Right Side: {right_fr:.2f} | Left Side: {left_fr:.2f} | Average: {avg_fr:.2f}",
            f"Your fatigue resistance score of {avg_fr:.2f} shows " + (
                "excellent endurance throughout the assessment." if 0.9 <= avg_fr <= 1.1 else
                "good endurance with some variation in performance." if 0.7 <= avg_fr <0.9 or 1.1 < avg_fr <=1.3 else
                "significant performance decrease that may indicate fatigue." if avg_fr>1.2 else 
                "significant performance increase may indicate adaptive issues."
            ),
            
            f'Optimal Range:Excellent: 0.9-1.1 | Good: 0.7-0.9 or 1.1-1.3 | Needs Improvement: <0.7 or >1.3',
            "A score close to 1.0 indicates consistent performance throughout the assessment. Scores significantly above or below 1.0 suggest either fatigue (decreasing performance) or adaptive isuues (in starting your body can't adapt to the drill).",
            'calculated as: (Hits in First 5 Targets) ÷ (Hits in Final 5 Targets)',

        )
        
        # Symmetry Score
        create_metric_box(
            "Symmetry Score",
            symmetry_score,
            "symmetry",
            "Indicates the balance between right and left side performance.",
            f"Score: {symmetry_score:.2f} (based on difference between right and left side hits)",
            f"Your symmetry score of {symmetry_score:.2f} indicates " + (
                "excellent balance between right and left performance." if symmetry_score > 0.9 else
                "good overall symmetry with some side-to-side differences." if symmetry_score > 0.7 else
                "significant differences between right and left side performance."
            ),
            f'Optimal Range:Excellent: >0.9 | Good: 0.7-0.9 | Needs Improvement: <0.7',
            "A score closer to 1.0 indicates better symmetry between sides. Lower scores suggest a notable difference in performance between right and left sides, which might indicate an area for focused training.",
            'Calculated as: 1 - (|Right Side Hits - Left Side Hits|/20)',
        )
    
        # # Add final note
        # note_style = ParagraphStyle(
        #     'Note',
        #     parent=styles['Normal'],
        #     fontSize=9,
        #     textColor=colors.HexColor('#666666'),
        #     leftIndent=20,
        #     rightIndent=20,
        #     spaceBefore=20
        # )
        
        # story.append(Paragraph(
        #     "<i>Note: These assessments are based on standardized performance metrics. Individual progress should be "
        #     "tracked over time for the most meaningful evaluation. Consult with your trainer for personalized "
        #     "training recommendations based on these results.</i>",
        #     note_style
        # ))
    
    # Update the main report generation to include the new interpretation section
    create_interpretation_section(story, right_metrics, left_metrics)
    create_recommendations_section(story, right_metrics, left_metrics, styles)
    story.append(PageBreak())
    create_conclusion_section(story, right_metrics, left_metrics, styles)
    story=create_final_branding_page(story,styles)
    
    # Build the PDF
    
    # Build the PDF
    doc.build(story)

# Example usage
if __name__ == "__main__":
    student_name = "devang babel"
    instructor_name = "Dr. aditya"
    left_scores = [1, 1, 1, 1, 1, 1,1,1,1,1,0]
    right_scores = [1, 1, 1, 1, 1, 1, 1,1,0]
    
    create_balance_report(student_name, instructor_name, left_scores, right_scores)
    import os
    os.startfile('balance_report_devang_babel.pdf')
    